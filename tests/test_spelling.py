"""Tests for the letter/digit lookup and intent handling."""
from unittest.mock import MagicMock

import pytest


def test_spell_simple_word_en(skill):
    words = skill._spell("cat", "en-us")
    assert words == ["Charlie", "Alfa", "Tango"]


def test_spell_uses_official_icao_spellings_not_alpha_or_juliet(skill):
    """A common mistake: 'Alpha'/'Juliet' instead of the official
    'Alfa'/'Juliett' ICAO spellings."""
    from nato_skill import NATO_WORDS
    assert NATO_WORDS["a"] == "Alfa"
    assert NATO_WORDS["j"] == "Juliett"


def test_spell_includes_digits(skill):
    words = skill._spell("a1", "en-us")
    assert words == ["Alfa", "One"]


def test_spell_danish_digit_words(skill):
    words = skill._spell("5", "da-dk")
    assert words == ["Fem"]


def test_spell_skips_non_alphanumeric(skill):
    """Spaces and punctuation are skipped rather than announced or
    erroring out."""
    words = skill._spell("a-b c", "en-us")
    assert words == ["Alfa", "Bravo", "Charlie"]


def test_spell_skips_danish_aeoeaa_not_in_nato_alphabet(skill):
    """The NATO alphabet only covers the 26 ASCII letters - Danish
    æ/ø/å aren't in it and are skipped, not a crash. 'søren' has
    s,ø,r,e,n - only 'ø' gets skipped, the rest spell out normally."""
    words = skill._spell("søren", "da-dk")
    assert words == ["Sierra", "Romeo", "Echo", "November"]


def test_spell_mixed_case_input(skill):
    assert skill._spell("CaT", "en-us") == ["Charlie", "Alfa", "Tango"]


def test_handle_spell_word_speaks_joined_words(skill):
    skill.speak_dialog = MagicMock()
    message = MagicMock()
    message.data = {"word": "cat"}
    skill.handle_spell_word(message)
    skill.speak_dialog.assert_called_once_with(
        "spelled_word", {"spelled": "Charlie, Alfa, Tango"})


def test_handle_spell_word_empty_input(skill):
    skill.speak_dialog = MagicMock()
    message = MagicMock()
    message.data = {"word": ""}
    skill.handle_spell_word(message)
    skill.speak_dialog.assert_called_once_with("nothing_to_spell")


def test_handle_spell_word_no_spellable_characters(skill):
    skill.speak_dialog = MagicMock()
    message = MagicMock()
    message.data = {"word": "!!!"}
    skill.handle_spell_word(message)
    skill.speak_dialog.assert_called_once_with(
        "nothing_spellable", {"word": "!!!"})



def test_every_template_names_the_alphabet():
    """issue #1: a plain "spell X" / "how do you spell X" belongs to OVOS's
    spelling skill - every template here asks for the NATO/phonetic alphabet."""
    from pathlib import Path
    words = {"en-us": ("nato", "phonetic", "radio"), "da-dk": ("nato", "fonetisk", "radio")}
    root = Path(__file__).resolve().parents[1] / "locale"
    for lang, markers in words.items():
        for line in (root / lang / "spell_word.intent").read_text().splitlines():
            if line.strip():
                assert any(m in line for m in markers), f"{lang}: {line!r}"
