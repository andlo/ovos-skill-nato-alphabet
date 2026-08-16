# Development

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
Pure lookup-table logic, no mocking needed for the spelling itself -
`test_spelling.py` covers the letter/digit tables directly, including
a dedicated regression test for the official ICAO spellings
("Alfa"/"Juliett", not "Alpha"/"Juliet" - an easy typo to make) and
the Danish æ/ø/å skip behavior.

## Adding a language

1. Add `locale/<lang>/spell_word.intent` - only the intent PHRASING
   needs translating ("spell X" -> whatever the equivalent is), NOT
   the NATO alphabet words themselves - see README for why.
2. Add `DIGIT_WORDS["<lang>"]` in `__init__.py` - the ten digit names
   in that language.
3. Add the standard dialog files (`spelled_word.dialog`,
   `nothing_to_spell.dialog`, `nothing_spellable.dialog`).
4. Add a `test_spell_<lang>_digit_words` case. Confirm
   `pytest tests/ -v` still passes.

## Versioning

`version.py` follows `VERSION_MAJOR.VERSION_MINOR.VERSION_BUILD[aVERSION_ALPHA]`.

## Releasing

Releases are tag-triggered (`v*`):
```bash
git add version.py
git commit -m "chore: bump version to 0.0.X"
git tag vX.Y.Z
git push && git push --tags
```
Triggers `.github/workflows/test.yml` then `.github/workflows/publish.yml`
(PyPI via trusted publishing - see `ovos-skill-convert`'s
DEVELOPMENT.md for the one-time PyPI setup needed before the first
tagged release).

## Style / conventions

- License: GPL-3.0-or-later (matches the other `andlo` skill repos).
- `locale/<lang-code>/` layout, `skill.json` inside each locale folder.
- Present design changes for review before implementing.
