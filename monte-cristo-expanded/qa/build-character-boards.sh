#!/bin/zsh

set -euo pipefail

project_root="${0:A:h:h:h}"
qa_dir="$project_root/monte-cristo-expanded/qa"
crops_dir="$(mktemp -d "${TMPDIR:-/tmp}/monte-cristo-character-qa.XXXXXX")"
trap 'rm -rf -- "$crops_dir"' EXIT
mkdir -p "$crops_dir"

head_crop() {
  local id="$1" label="$2" source="$3" size="$4" x="$5" y="$6"
  ffmpeg -loglevel error -y -i "$source" \
    -vf "crop=${size}:${size}:${x}:${y},scale=220:220" \
    -frames:v 1 "$crops_dir/head-${id}.png"
}

body_crop() {
  local id="$1" label="$2" source="$3" width="$4" x="$5"
  local height="${6:-1024}" y="${7:-0}"
  ffmpeg -loglevel error -y -i "$source" \
    -vf "crop=${width}:${height}:${x}:${y},scale=200:290:force_original_aspect_ratio=decrease,pad=220:300:(ow-iw)/2:(oh-ih)/2:color=0xf2e8d5,format=gray" \
    -frames:v 1 "$crops_dir/body-${id}.png"
}

old_refs="$project_root/monte-cristo/refs"
new_refs="$project_root/monte-cristo-expanded/refs"

head_crop 01 "Young Edmond" "$old_refs/01-edmond-young.png" 360 1190 170
head_crop 02 "Prison Edmond" "$old_refs/02-edmond-prison.png" 360 1170 160
head_crop 03 "The Count" "$new_refs/02-count-v2.png" 360 910 50
head_crop 04 "Faria" "$old_refs/04-faria.png" 360 1130 10
head_crop 05 "Villefort" "$new_refs/01-villefort-1815-v2.png" 360 910 40
head_crop 06 "Mercedes 1815" "$old_refs/09-mercedes-1815.png" 360 1170 150
head_crop 07 "Mercedes 1838" "$new_refs/07-mercedes-1838-v2.png" 360 1170 150
head_crop 08 "Louis Dantes" "$new_refs/04-louis-dantes-v2.png" 360 1050 40
head_crop 09 "Danglars" "$old_refs/11-danglars-1815.png" 360 460 120
head_crop 10 "Fernand" "$new_refs/05-fernand-1815-v2.png" 360 1060 50
head_crop 11 "Caderousse" "$old_refs/13-caderousse-1815.png" 360 1130 140
head_crop 12 "Morrel" "$old_refs/14-morrel-household.png" 360 240 70
head_crop 13 "Julie" "$new_refs/06-julie-emmanuel-v2.png" 360 350 70
head_crop 14 "Emmanuel" "$new_refs/06-julie-emmanuel-v2.png" 360 860 70
head_crop 15 "Jacopo" "$new_refs/03-jacopo-v2.png" 360 1010 20
head_crop 16 "Smuggler captain" "$old_refs/15-jacopo-captain.png" 360 1160 70
head_crop 17 "Busoni" "$new_refs/08-busoni-wilmore-v2.png" 360 430 70
head_crop 18 "Wilmore" "$new_refs/08-busoni-wilmore-v2.png" 360 860 70
head_crop 19 "Leclere" "$new_refs/09-leclere-noirtier.png" 360 410 170
head_crop 20 "Noirtier" "$new_refs/09-leclere-noirtier.png" 360 1120 100
head_crop 21 "Renee" "$new_refs/10-renee-marquise.png" 360 420 90
head_crop 22 "Marquise" "$new_refs/10-renee-marquise.png" 360 860 100
head_crop 23 "Principal guard" "$new_refs/11-principal-guard-jailer.png" 360 360 140
head_crop 24 "Jailer" "$new_refs/11-principal-guard-jailer.png" 360 820 130
head_crop 25 "Intake clerk" "$new_refs/12-clerk-governor.png" 360 360 130
head_crop 26 "Governor" "$new_refs/12-clerk-governor.png" 360 840 100

body_crop 01 "Young Edmond" "$old_refs/01-edmond-young.png" 400 0
body_crop 02 "Prison Edmond" "$old_refs/02-edmond-prison.png" 420 0
body_crop 03 "The Count" "$new_refs/02-count-v2.png" 350 0
body_crop 04 "Faria" "$old_refs/04-faria.png" 430 0
body_crop 05 "Villefort" "$new_refs/01-villefort-1815-v2.png" 360 0
body_crop 06 "Mercedes 1815" "$old_refs/09-mercedes-1815.png" 420 0
body_crop 07 "Mercedes 1838" "$new_refs/07-mercedes-1838-v2.png" 380 0
body_crop 08 "Louis Dantes" "$new_refs/04-louis-dantes-v2.png" 380 0
body_crop 09 "Danglars" "$old_refs/11-danglars-1815.png" 390 0
body_crop 10 "Fernand" "$new_refs/05-fernand-1815-v2.png" 430 0
body_crop 11 "Caderousse" "$old_refs/13-caderousse-1815.png" 500 0
body_crop 12 "Morrel" "$old_refs/14-morrel-household.png" 360 0
body_crop 13 "Julie" "$new_refs/06-julie-emmanuel-v2.png" 420 0
body_crop 14 "Emmanuel" "$new_refs/06-julie-emmanuel-v2.png" 406 1130
body_crop 15 "Jacopo" "$new_refs/03-jacopo-v2.png" 400 0
body_crop 16 "Smuggler captain" "$old_refs/15-jacopo-captain.png" 330 760 780 0
body_crop 17 "Busoni" "$new_refs/08-busoni-wilmore-v2.png" 400 0
body_crop 18 "Wilmore" "$new_refs/08-busoni-wilmore-v2.png" 366 1170
body_crop 19 "Leclere" "$new_refs/09-leclere-noirtier.png" 370 0
body_crop 20 "Noirtier" "$new_refs/09-leclere-noirtier.png" 350 780
body_crop 21 "Renee" "$new_refs/10-renee-marquise.png" 360 0
body_crop 22 "Marquise" "$new_refs/10-renee-marquise.png" 356 1180
body_crop 23 "Principal guard" "$new_refs/11-principal-guard-jailer.png" 350 0
body_crop 24 "Jailer" "$new_refs/11-principal-guard-jailer.png" 356 1180
body_crop 25 "Intake clerk" "$new_refs/12-clerk-governor.png" 360 0
body_crop 26 "Governor" "$new_refs/12-clerk-governor.png" 366 1170

ffmpeg -loglevel error -y -framerate 1 -pattern_type glob \
  -i "$crops_dir/head-*.png" \
  -vf "tile=7x4:padding=8:margin=8:color=0x2b2723" \
  -frames:v 1 "$qa_dir/character-heads-board.png"

ffmpeg -loglevel error -y -framerate 1 -pattern_type glob \
  -i "$crops_dir/body-*.png" \
  -vf "tile=7x4:padding=8:margin=8:color=0x2b2723" \
  -frames:v 1 "$qa_dir/character-silhouettes-board.png"

adversarial_board() {
  local output="$1" a="$2" b="$3" c="$4" d="$5"
  ffmpeg -loglevel error -y \
    -i "$crops_dir/head-${a}.png" -i "$crops_dir/head-${b}.png" \
    -i "$crops_dir/head-${c}.png" -i "$crops_dir/head-${d}.png" \
    -i "$crops_dir/body-${a}.png" -i "$crops_dir/body-${b}.png" \
    -i "$crops_dir/body-${c}.png" -i "$crops_dir/body-${d}.png" \
    -filter_complex "[0][1][2][3]hstack=inputs=4[top];[4][5][6][7]hstack=inputs=4[bottom];[top][bottom]vstack=inputs=2" \
    -frames:v 1 "$qa_dir/$output"
}

adversarial_board adversarial-edmond-villefort.png 01 05 10 09
adversarial_board adversarial-formal-men.png 03 05 14 18
adversarial_board adversarial-escape-men.png 01 02 15 16
adversarial_board adversarial-fathers-and-daughters.png 08 04 06 13

echo "Character comparison boards written to $qa_dir"
