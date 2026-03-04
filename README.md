# obj-viewer
load obj, view with pyglet

## Project history

- Initial commit: `2021-10-23`
- Demo refresh pass: `2026-03-04`
- Notes: migrated to `uv` workflow and updated legacy demo code so demos run again on current Python/pyglet.

## Run with uv

```bash
uv sync
uv run obj-viewer --demo model
uv run obj-viewer --demo model --model logo3d
```

Available demos: `model`, `shapes`, `tri`, `field`, `shader`.
Model assets for `--demo model`: `cube`, `logo3d`.
