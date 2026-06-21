#!/bin/bash

for dir in */; do
  folder_name="${dir%/}"
  cat "$folder_name/$folder_name-final-report.md" "$folder_name/$folder_name-facets.md" "$folder_name/$folder_name-markers.md" > "$folder_name/$folder_name-combined.md"
done
