#!/bin/zsh

set -u

repo_root="/Users/andresrodriguez/Documents/nano"
qa_dir="$repo_root/monte-cristo-vol2/qa/references/sheet-11"
source_file="$qa_dir/build-silhouette-board-v2.swift"
runner_file="$qa_dir/sheet11-v2-runner"
log_file="$qa_dir/terminal-v2.log"
status_file="$qa_dir/terminal-v2.status"

exec >"$log_file" 2>&1

echo "Sheet 11 deterministic Vision extraction"
date -u '+UTC start: %Y-%m-%dT%H:%M:%SZ'
echo "Compiling: $source_file"

/usr/bin/swiftc "$source_file" -o "$runner_file"
run_status=$?

if [[ $run_status -eq 0 ]]; then
  echo "Running outside the ChatGPT desktop sandbox"
  "$runner_file"
  run_status=$?
fi

echo "Exit status: $run_status"
date -u '+UTC end: %Y-%m-%dT%H:%M:%SZ'
echo "$run_status" >"$status_file"
exit "$run_status"
