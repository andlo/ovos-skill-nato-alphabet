# NatoAlphabet

Spells words using the NATO phonetic alphabet (Alpha, Bravo, Charlie...) - 'spell Andreas' -> 'Alfa, November, Delta, Romeo, Echo, Alfa, Sierra'. Genuinely practical for dictating serial numbers, emails, or names over the phone. Pure text-to-table lookup, zero ambiguity, no external dependencies at all.

> **This is a skeleton only - not implemented yet.** Repo, structure,
> and design notes are in place; the actual skill logic hasn't been
> written. See "Design notes" in [DEVELOPMENT.md](DEVELOPMENT.md).

## Why this exists

Nothing like this exists in the OVOS ecosystem yet (checked before starting). Same architectural shape as ovos-skill-convert: a fixed lookup table, no fuzzy logic needed, en-us + da-dk locale files.

## Planned usage (not yet functional)
```
"spell Andreas"
"how do you spell hello using the phonetic alphabet"
```

## Install

Not yet published to PyPI.

## Development

See [DEVELOPMENT.md](DEVELOPMENT.md).

## Category
**Utility**

## Tags
#spelling #nato #phonetic-alphabet #utility
