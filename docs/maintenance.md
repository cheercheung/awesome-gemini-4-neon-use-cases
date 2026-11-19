# Maintenance

The structured case index is the source of truth for case identity, order,
source attribution, dates, prompt evidence, and media. Keep the English README
and all translated editions consistent with it.

## Updating cases

1. Record the source and its scope, then review the complete evidence before
   adding a project, workflow, or evaluation.
2. Match reposts and follow-ups to existing case IDs. Append new case numbers
   consecutively and preserve published IDs.
3. Keep the original prompt only when the source confirms the exact text.
4. Preserve each attached image and video in the reviewed media set. Keep
   comparison visuals together. Link posters to verified playback.
5. Update every affected language. Keep numeric claims, source links, dates,
   model names, roles, anchors, and prompt text synchronized.

## Validation

Run `git diff --check`. Verify the complete README and data case set, the
localized structure and prose, source-media reconciliation, link targets,
image origins, and playable videos. Inspect the GitHub desktop and narrow
renders and record the results against the reviewed commit.

Follow the [contribution guide](../CONTRIBUTING.md) for reporting corrections.

The public case data is in `data/use-cases.json`, and translations are in
`data/localizations/`. Regenerate the display files with
`python3 scripts/build_readmes.py` after editing this data.
Run `python3 scripts/build_readmes.py --check` to confirm all display files
match the data.
