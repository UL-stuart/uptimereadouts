# Options IT Usage and Performance Stats

Source files:

- `options-it-airtable-summary.csv`
- `options-it-drill-usage.csv`

## Summary

| Metric | Value | Source / calculation |
| --- | ---: | --- |
| Total PIR Sessions | 20	 | `options-it-airtable-summary.csv`, `Total sessions` row |
| Total Drills | 21 | Unique drill names in `options-it-drill-usage.csv` |
| Average GUOT score | 9.0 | Average of 83 non-empty `GUOT` scores |
| Total Drill Sessions | 96 | Rows in `options-it-drill-usage.csv` |
| Total Participants | 21 | Unique non-empty `player` values in `options-it-drill-usage.csv` |
| Drills per Participant | 4.6 | 96 drill sessions / 21 participants |

## Drills Experienced by Player

| Player | Drills experienced |
| --- | ---: |
| lucy.mccormack | 10 |
| amelia.horwood | 6 |
| ciaran.hurley | 6 |
| ellie.walsh | 6 |
| jamie.dow | 6 |
| jessica.mcdonald | 6 |
| mark.mcgarry | 6 |
| aoife.breen | 5 |
| donnchadh.tierney | 5 |
| jack.walsh | 5 |
| leah.murphy | 5 |
| patrick.collins | 5 |
| elsa.savage | 4 |
| emma.allsopp | 4 |
| james.sheppy | 4 |
| ruairi.corrigan | 4 |
| caoimhe.kelly | 3 |
| ritchie.mcgrath | 3 |
| ciara.scullion | 1 |
| peter.graham | 1 |
| zach.davis | 1 |

## Notes

- GUOT average excludes null, missing, or blank scores.
- `options-it-airtable-summary.csv` also contains `PIR in session plan = 20`; the headline PIR sessions figure above uses the file's `Total sessions` row.
