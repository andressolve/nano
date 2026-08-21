#!/usr/bin/env swift

import AppKit
import CoreImage
import CoreVideo
import CryptoKit
import Foundation
import Vision

struct SourceSpec {
    let id: String
    let character: String
    let path: String
    let sha256: String
    let crop: CGRect
    let headTopY: Int
    let floorY: Int
}

let root = URL(fileURLWithPath: #filePath)
    .deletingLastPathComponent()
    .deletingLastPathComponent()
    .deletingLastPathComponent()
    .deletingLastPathComponent()
    .deletingLastPathComponent()
let qaDirectory = root.appendingPathComponent("monte-cristo-vol2/qa/references/sheet-11")
let maskDirectory = qaDirectory.appendingPathComponent("masks-v2")
let outputURL = root.appendingPathComponent("monte-cristo-vol2/refs/11-silhouette-board.png")
let manifestURL = qaDirectory.appendingPathComponent("manifest-v2.json")

let canvasWidth = 1536
let canvasHeight = 1024
let cellWidth = 192
let targetBodyHeight = 370.0
let targetFloorY = 697.0
let ground = NSColor(calibratedRed: 224.0 / 255.0, green: 219.0 / 255.0, blue: 211.0 / 255.0, alpha: 1)
let silhouette = NSColor(calibratedRed: 38.0 / 255.0, green: 36.0 / 255.0, blue: 34.0 / 255.0, alpha: 1)

let sources = [
    SourceSpec(id: "01", character: "Count", path: "monte-cristo-vol2/refs/approved/01-count-1838.png", sha256: "2e38a28eb27183c7bc9addbbbc2b9ccdfefb8c7a3e9d5ac945e81c0a424b3bd0", crop: CGRect(x: 560, y: 30, width: 340, height: 975), headTopY: 55, floorY: 985),
    SourceSpec(id: "02", character: "Mercédès", path: "monte-cristo-vol2/refs/approved/02-mercedes-1838.png", sha256: "8113d7b65a0916c8bf75d12bd1fcf180fc9a31152a11c3f2151eb968e4210821", crop: CGRect(x: 400, y: 75, width: 445, height: 935), headTopY: 100, floorY: 990),
    SourceSpec(id: "03", character: "Fernand", path: "monte-cristo-vol2/refs/approved/03-fernand-1838.png", sha256: "487f21e1de98136ddc16fcd7aa44d69d0fd659178de417ed282dd30486ea0a40", crop: CGRect(x: 510, y: 30, width: 420, height: 975), headTopY: 55, floorY: 985),
    SourceSpec(id: "04", character: "Albert", path: "monte-cristo-vol2/refs/approved/04-albert.png", sha256: "3ff9d03308e7f79d5b217f90e8437067a8e407c0f3347902a87db4fb0f54dbee", crop: CGRect(x: 500, y: 30, width: 370, height: 975), headTopY: 50, floorY: 985),
    SourceSpec(id: "05", character: "Haydée", path: "monte-cristo-vol2/refs/approved/05-haydee.png", sha256: "0c717b0aaf9eac65f515e604b93112ad7cd7560579631a423acbec947ca4efbf", crop: CGRect(x: 490, y: 55, width: 370, height: 945), headTopY: 80, floorY: 980),
    SourceSpec(id: "06", character: "Danglars", path: "monte-cristo-vol2/refs/approved/06-danglars-1838.png", sha256: "626f71c601069032624654958a24b06dfc33974d290d6c9d09d627f3f1e4beb9", crop: CGRect(x: 480, y: 50, width: 400, height: 950), headTopY: 75, floorY: 980),
    SourceSpec(id: "07", character: "Beauchamp", path: "monte-cristo-vol2/refs/approved/07-beauchamp.png", sha256: "58ba63bf5b77fdf31c585da888461c143474c750d0fa8b2bf7cdab218f38d834", crop: CGRect(x: 485, y: 20, width: 330, height: 985), headTopY: 35, floorY: 990),
    SourceSpec(id: "08", character: "Villefort", path: "monte-cristo-vol2/refs/approved/08-villefort-1838.png", sha256: "46e31557dd3fd34d3a103e028721869dba5dc0b16874bb40dc00f0982c262e75", crop: CGRect(x: 640, y: 50, width: 350, height: 955), headTopY: 75, floorY: 985),
]

func sha256(_ url: URL) throws -> String {
    let digest = SHA256.hash(data: try Data(contentsOf: url))
    return digest.map { String(format: "%02x", $0) }.joined()
}

func loadCGImage(_ url: URL) throws -> CGImage {
    guard let image = NSImage(contentsOf: url) else {
        throw NSError(domain: "Sheet11", code: 1, userInfo: [NSLocalizedDescriptionKey: "Cannot load \(url.path)"])
    }
    var rect = CGRect(origin: .zero, size: image.size)
    guard let cgImage = image.cgImage(forProposedRect: &rect, context: nil, hints: nil) else {
        throw NSError(domain: "Sheet11", code: 2, userInfo: [NSLocalizedDescriptionKey: "Cannot decode \(url.path)"])
    }
    return cgImage
}

enum MaskDecodeMode {
    case instanceLabels
    case normalizedAlpha
}

func pixelBytes(_ buffer: CVPixelBuffer, mode: MaskDecodeMode) throws -> (width: Int, height: Int, bytes: [UInt8]) {
    let format = CVPixelBufferGetPixelFormatType(buffer)
    CVPixelBufferLockBaseAddress(buffer, .readOnly)
    defer { CVPixelBufferUnlockBaseAddress(buffer, .readOnly) }
    guard let base = CVPixelBufferGetBaseAddress(buffer) else {
        throw NSError(domain: "Sheet11", code: 4, userInfo: [NSLocalizedDescriptionKey: "Vision mask has no base address"])
    }
    let width = CVPixelBufferGetWidth(buffer)
    let height = CVPixelBufferGetHeight(buffer)
    let stride = CVPixelBufferGetBytesPerRow(buffer)
    var bytes = [UInt8](repeating: 0, count: width * height)

    if format == kCVPixelFormatType_OneComponent8 {
        for y in 0..<height {
            let row = base.advanced(by: y * stride).assumingMemoryBound(to: UInt8.self)
            for x in 0..<width { bytes[y * width + x] = row[x] }
        }
    } else if format == kCVPixelFormatType_OneComponent32Float {
        for y in 0..<height {
            let row = base.advanced(by: y * stride).assumingMemoryBound(to: Float.self)
            for x in 0..<width {
                let raw = row[x].isFinite ? row[x] : 0
                let decoded: Float
                switch mode {
                case .instanceLabels:
                    decoded = raw.rounded()
                case .normalizedAlpha:
                    decoded = (raw * 255).rounded()
                }
                bytes[y * width + x] = UInt8(clamping: Int(decoded))
            }
        }
    } else {
        throw NSError(domain: "Sheet11", code: 3, userInfo: [NSLocalizedDescriptionKey: "Unexpected Vision mask pixel format \(format)"])
    }
    return (width, height, bytes)
}

func largestInstance(_ observation: VNInstanceMaskObservation) throws -> (label: Int, area: Int) {
    let lowResolution = try pixelBytes(observation.instanceMask, mode: .instanceLabels)
    var counts: [Int: Int] = [:]
    for value in lowResolution.bytes where value != 0 {
        counts[Int(value), default: 0] += 1
    }
    let allowed = Set(observation.allInstances.map { Int($0) })
    guard let best = counts
        .filter({ allowed.contains($0.key) })
        .max(by: { $0.value < $1.value }) else {
        throw NSError(domain: "Sheet11", code: 5, userInfo: [NSLocalizedDescriptionKey: "Vision found no person instance"])
    }
    return (best.key, best.value)
}

func makeMaskImage(width: Int, height: Int, bytes: [UInt8]) throws -> CGImage {
    let data = Data(bytes)
    guard let provider = CGDataProvider(data: data as CFData),
          let image = CGImage(
            width: width,
            height: height,
            bitsPerComponent: 8,
            bitsPerPixel: 8,
            bytesPerRow: width,
            space: CGColorSpaceCreateDeviceGray(),
            bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue),
            provider: provider,
            decode: nil,
            shouldInterpolate: true,
            intent: .defaultIntent
          ) else {
        throw NSError(domain: "Sheet11", code: 6, userInfo: [NSLocalizedDescriptionKey: "Cannot construct mask CGImage"])
    }
    return image
}

func savePNG(_ image: CGImage, to url: URL) throws {
    let representation = NSBitmapImageRep(cgImage: image)
    guard let data = representation.representation(using: .png, properties: [:]) else {
        throw NSError(domain: "Sheet11", code: 7, userInfo: [NSLocalizedDescriptionKey: "Cannot encode PNG \(url.path)"])
    }
    try data.write(to: url, options: .atomic)
}

try FileManager.default.createDirectory(at: qaDirectory, withIntermediateDirectories: true)
try FileManager.default.createDirectory(at: maskDirectory, withIntermediateDirectories: true)

let colorSpace = CGColorSpaceCreateDeviceRGB()
guard let context = CGContext(
    data: nil,
    width: canvasWidth,
    height: canvasHeight,
    bitsPerComponent: 8,
    bytesPerRow: canvasWidth * 4,
    space: colorSpace,
    bitmapInfo: CGBitmapInfo.byteOrder32Big.rawValue | CGImageAlphaInfo.noneSkipLast.rawValue
) else {
    throw NSError(domain: "Sheet11", code: 8, userInfo: [NSLocalizedDescriptionKey: "Cannot create board context"])
}

// Use top-left coordinates for all deterministic crop placements.
context.translateBy(x: 0, y: CGFloat(canvasHeight))
context.scaleBy(x: 1, y: -1)
context.setFillColor(ground.cgColor)
context.fill(CGRect(x: 0, y: 0, width: canvasWidth, height: canvasHeight))
context.interpolationQuality = .high

var manifestSources: [[String: Any]] = []

for (index, spec) in sources.enumerated() {
    let sourceURL = root.appendingPathComponent(spec.path)
    let actualHash = try sha256(sourceURL)
    guard actualHash == spec.sha256 else {
        throw NSError(domain: "Sheet11", code: 9, userInfo: [NSLocalizedDescriptionKey: "Approved source hash mismatch for \(spec.path)"])
    }
    let source = try loadCGImage(sourceURL)
    guard source.width == 1536 && source.height == 1024 else {
        throw NSError(domain: "Sheet11", code: 10, userInfo: [NSLocalizedDescriptionKey: "Unexpected source size for \(spec.path)"])
    }
    guard let crop = source.cropping(to: spec.crop) else {
        throw NSError(domain: "Sheet11", code: 11, userInfo: [NSLocalizedDescriptionKey: "Cannot crop \(spec.path)"])
    }

    let request = VNGeneratePersonInstanceMaskRequest()
    request.revision = VNGeneratePersonInstanceMaskRequestRevision1
    let handler = VNImageRequestHandler(cgImage: crop, orientation: .up, options: [:])
    try handler.perform([request])
    guard let observation = request.results?.first else {
        throw NSError(domain: "Sheet11", code: 12, userInfo: [NSLocalizedDescriptionKey: "Vision found no person in \(spec.character)"])
    }
    let selected = try largestInstance(observation)
    let selectedInstances = IndexSet(integer: selected.label)
    let scaledBuffer = try observation.generateScaledMaskForImage(forInstances: selectedInstances, from: handler)
    var scaled = try pixelBytes(scaledBuffer, mode: .normalizedAlpha)
    guard scaled.width == crop.width && scaled.height == crop.height else {
        throw NSError(domain: "Sheet11", code: 13, userInfo: [NSLocalizedDescriptionKey: "Vision scaled mask size mismatch for \(spec.character)"])
    }

    // Remove only pixels below the recorded source floor. No other mask repair,
    // tracing, painting, contour adjustment, or pose correction is performed.
    let floorRelative = spec.floorY - Int(spec.crop.minY)
    if floorRelative + 1 < scaled.height {
        for y in (floorRelative + 1)..<scaled.height {
            for x in 0..<scaled.width { scaled.bytes[y * scaled.width + x] = 0 }
        }
    }

    // Vision's L00f mask is a continuous confidence map. The Sheet 11
    // silhouette contract is binary, and the manifest already audits the
    // foreground at >=128. Apply that same fixed decision to every pixel before
    // composition so no low-confidence grey haze or interior tone survives.
    for position in scaled.bytes.indices {
        scaled.bytes[position] = scaled.bytes[position] >= 128 ? 255 : 0
    }

    var minX = scaled.width
    var minY = scaled.height
    var maxX = -1
    var maxY = -1
    var selectedPixels = 0
    for y in 0..<scaled.height {
        for x in 0..<scaled.width where scaled.bytes[y * scaled.width + x] >= 128 {
            minX = min(minX, x)
            minY = min(minY, y)
            maxX = max(maxX, x)
            maxY = max(maxY, y)
            selectedPixels += 1
        }
    }
    guard maxX >= minX && maxY >= minY else {
        throw NSError(domain: "Sheet11", code: 14, userInfo: [NSLocalizedDescriptionKey: "Empty high-resolution Vision mask for \(spec.character)"])
    }

    let uprightMaskImage = try makeMaskImage(width: scaled.width, height: scaled.height, bytes: scaled.bytes)
    let maskURL = maskDirectory.appendingPathComponent("mask-\(spec.id).png")
    try savePNG(uprightMaskImage, to: maskURL)

    // The decoded and saved Vision mask is upright in top-left row order. The
    // board CGContext is globally transformed to top-left user coordinates,
    // while clip(to:mask:) samples CGImage mask rows in Quartz image order.
    // Reverse the rows exactly once for clipping so the placed silhouette
    // remains upright. This changes orientation only, never contour pixels.
    var quartzClipBytes = [UInt8](repeating: 0, count: scaled.bytes.count)
    for y in 0..<scaled.height {
        let sourceRow = y * scaled.width
        let destinationRow = (scaled.height - 1 - y) * scaled.width
        quartzClipBytes.replaceSubrange(
            destinationRow..<(destinationRow + scaled.width),
            with: scaled.bytes[sourceRow..<(sourceRow + scaled.width)]
        )
    }
    let quartzClipMaskImage = try makeMaskImage(width: scaled.width, height: scaled.height, bytes: quartzClipBytes)

    let bodyHeight = Double(spec.floorY - spec.headTopY)
    let scale = targetBodyHeight / bodyHeight
    let maskCenterX = Double(minX + maxX + 1) / 2.0
    let placementX = Double(index * cellWidth) + Double(cellWidth) / 2.0 - maskCenterX * scale
    let placementY = targetFloorY - Double(floorRelative) * scale
    let destination = CGRect(
        x: placementX,
        y: placementY,
        width: Double(scaled.width) * scale,
        height: Double(scaled.height) * scale
    )
    let placedBBox = [
        placementX + Double(minX) * scale,
        placementY + Double(minY) * scale,
        placementX + Double(maxX + 1) * scale,
        placementY + Double(maxY + 1) * scale,
    ]
    let cellLeft = Double(index * cellWidth)
    let cellRight = Double((index + 1) * cellWidth)
    guard placedBBox[0] >= cellLeft && placedBBox[2] <= cellRight else {
        throw NSError(domain: "Sheet11", code: 15, userInfo: [NSLocalizedDescriptionKey: "Vision silhouette crosses cell for \(spec.character): \(placedBBox)"])
    }

    context.saveGState()
    context.clip(to: destination, mask: quartzClipMaskImage)
    context.setFillColor(silhouette.cgColor)
    context.fill(destination)
    context.restoreGState()

    manifestSources.append([
        "order": index + 1,
        "id": spec.id,
        "character": spec.character,
        "source_path": spec.path,
        "source_sha256": actualHash,
        "source_size": [source.width, source.height],
        "source_mode": "RGB",
        "crop_box_xyxy": [Int(spec.crop.minX), Int(spec.crop.minY), Int(spec.crop.maxX), Int(spec.crop.maxY)],
        "extraction": [
            "framework": "macOS Vision",
            "request": "VNGeneratePersonInstanceMaskRequest",
            "revision": Int(VNGeneratePersonInstanceMaskRequestRevision1),
            "selection": "largest automatically detected person instance in the exact crop",
            "selected_instance_label": selected.label,
            "selected_instance_low_resolution_area": selected.area,
            "scaled_mask_threshold_bbox_xyxy": [minX, minY, maxX + 1, maxY + 1],
            "scaled_mask_selected_pixels_at_128": selectedPixels,
            "binary_mask_decision": "decoded alpha >=128 becomes 255; decoded alpha <128 becomes 0",
            "floor_rule": "clear mask rows strictly below recorded source floor",
            "quartz_clip_orientation": "upright binary evidence mask; rows reversed exactly once only for clip(to:mask:) under the existing top-left CGContext transform",
            "mask_path": maskURL.path.replacingOccurrences(of: root.path + "/", with: ""),
            "mask_sha256": try sha256(maskURL),
        ],
        "normalization_landmarks": ["head_top_y": spec.headTopY, "floor_y": spec.floorY],
        "scale": scale,
        "crop_placement_xy": [placementX, placementY],
        "placed_silhouette_bbox_xyxy": placedBBox,
        "cell_xyxy": [cellLeft, 0.0, cellRight, Double(canvasHeight)],
    ])
}

guard let boardImage = context.makeImage() else {
    throw NSError(domain: "Sheet11", code: 16, userInfo: [NSLocalizedDescriptionKey: "Cannot finalize board image"])
}
try savePNG(boardImage, to: outputURL)
let outputHash = try sha256(outputURL)

let manifest: [String: Any] = [
    "artifact": "Sheet 11 — grayscale silhouette board",
    "version": 2,
    "method": "automatic local macOS Vision person-instance segmentation, recorded-floor clear, uniform scale, flat silhouette conversion, and placement",
    "generative_operation": false,
    "network_or_api": false,
    "execution_route": "run-v2-in-terminal.command outside the ChatGPT desktop sandbox",
    "vision_mask_pixel_format_support": [
        "L008 / kCVPixelFormatType_OneComponent8",
        "L00f / kCVPixelFormatType_OneComponent32Float; label rounding for instance maps and normalized 0–1 alpha scaling for generated masks",
    ],
    "composition_correction": [
        "binary_mask_cutoff": ">=128 foreground; <128 background",
        "orientation": "decoded masks remain upright; a one-time vertical row reversal is used only for Quartz clipping so the globally top-left board context does not invert them",
        "unchanged": "approved sources and hashes, crop boxes, Vision request/revision, largest-instance selection, recorded floor landmarks, target body height/floor, order, cells, silhouette RGB, and ground RGB",
    ],
    "manual_contour_operation": false,
    "canvas": ["width": canvasWidth, "height": canvasHeight, "mode": "RGB", "format": "PNG"],
    "ground_rgb": [224, 219, 211],
    "silhouette_rgb": [38, 36, 34],
    "order": "01 Count, 02 Mercédès, 03 Fernand, 04 Albert, 05 Haydée, 06 Danglars, 07 Beauchamp, 08 Villefort",
    "normalization": [
        "target_body_height_px": targetBodyHeight,
        "target_floor_y": targetFloorY,
        "mask_scaling": "Core Graphics high-quality interpolation during deterministic placement",
        "interior": "one flat dark RGB value; no source color or interior detail",
    ],
    "sources": manifestSources,
    "output_path": outputURL.path.replacingOccurrences(of: root.path + "/", with: ""),
    "output_sha256": outputHash,
]
let manifestData = try JSONSerialization.data(withJSONObject: manifest, options: [.prettyPrinted, .sortedKeys, .withoutEscapingSlashes])
try manifestData.write(to: manifestURL, options: .atomic)

print("wrote \(outputURL.path)")
print("wrote \(manifestURL.path)")
print("output_sha256 \(outputHash)")
