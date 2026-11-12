#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
output="$script_dir/combined-supplement-essays.md"
temporary=$(mktemp "${TMPDIR:-/tmp}/aditya-supplements.XXXXXX")
trap 'rm -f "$temporary"' EXIT HUP INT TERM

{
  printf '# Aditya Balaji: Combined Supplemental Essays\n\n'
  printf '> Generated from the university files listed below. Edit the individual files, then run `sh aditya/supplements/sync-combined.sh`.\n\n'

  for source in \
    "$script_dir/us/mit/essays.md" \
    "$script_dir/us/stanford/essays.md" \
    "$script_dir/us/ea/purdue/essays.md" \
    "$script_dir/us/virginia-tech/essays.md" \
    "$script_dir/us/ea/uiuc/essays.md" \
    "$script_dir/us/umd/essays.md" \
    "$script_dir/us/ea/umass/essays.md" \
    "$script_dir/uk/ucas.md"
  do
    printf '\n---\n\n'
    sed -n '1,$p' "$source"
    printf '\n'
  done
} > "$temporary"

mv "$temporary" "$output"
trap - EXIT HUP INT TERM

