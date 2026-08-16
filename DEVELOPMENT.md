# Development

## Status

This is a skeleton, not a working skill yet. Structure (repo, CI,
locale folders, license, packaging) is in place; the real
`NatoAlphabet` logic in `__init__.py` is a placeholder that just
speaks a "not implemented" dialog.

## Design notes (resolve before implementing)

- Nothing like this exists in the OVOS ecosystem yet (checked before starting). Same architectural shape as ovos-skill-convert: a fixed lookup table, no fuzzy logic needed, en-us + da-dk locale files.
- Follow the same review-before-build process used for
  `ovos-skill-convert` and `ovos-skill-sound-like`: sketch the actual
  intent grammar, any external data/sample sourcing, and known
  tricky edge cases, and check them over before writing real code.

## Setup
```bash
git clone https://github.com/andlo/ovos-skill-nato-alphabet.git
cd ovos-skill-nato-alphabet
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
pip install -r requirements-test.txt
```

## Running tests
```bash
pytest tests/ -v
```
Currently just a smoke test confirming the skill imports and loads -
real test coverage arrives with real implementation.

## Versioning

`version.py` follows `VERSION_MAJOR.VERSION_MINOR.VERSION_BUILD[aVERSION_ALPHA]`.
Stays on **0.0.x** through the skeleton phase and initial
implementation, same convention as `ovos-skill-convert` and
`ovos-skill-sound-like`.

## Style / conventions

- License: GPL-3.0-or-later (matches the other `andlo` skill repos).
- `locale/<lang-code>/` layout, `skill.json` inside each locale folder.
- Present the real design (intent grammar, data sourcing, edge cases)
  for review before implementing - not just for translations.
