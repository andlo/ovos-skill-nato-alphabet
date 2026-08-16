"""
skill OVOS NATO Alphabet
Copyright (C) 2026  Andreas Lorensen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

---

Spells a word using the NATO/ICAO phonetic alphabet - "spell Andreas"
-> "Alfa, November, Delta, Romeo, Echo, Alfa, Sierra". Pure text-to-
table lookup, zero ambiguity, no external dependencies at all.

THE ALPHABET WORDS THEMSELVES ARE NOT TRANSLATED
--------------------------------------------------------
NATO_WORDS uses the official ICAO spelling (note: "Alfa" and
"Juliett", not "Alpha"/"Juliet" - deliberate spellings chosen
internationally to avoid pronunciation ambiguity across languages).
This is a single international standard, the same words regardless of
who's speaking - a Danish speaker asking "stav Andreas" still gets
"Alfa, November, Delta..." back, not a Danish-language equivalent
alphabet. Only the INTENT PHRASING ("spell X" vs "stav X") is
localized, not the alphabet content itself.

DIGITS
------
NATO officially only standardizes the 26 letters. Digits are spoken
as their plain number word in the device's language (not a separate
"aviation numeral" pronunciation like "niner" for 9 - that's a
different, narrower radiotelephony convention this skill doesn't
attempt to replicate).
"""

from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler

# Official ICAO/NATO phonetic alphabet - note "Alfa" and "Juliett"
# spellings, not "Alpha"/"Juliet"
NATO_WORDS = {
    "a": "Alfa", "b": "Bravo", "c": "Charlie", "d": "Delta", "e": "Echo",
    "f": "Foxtrot", "g": "Golf", "h": "Hotel", "i": "India", "j": "Juliett",
    "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November", "o": "Oscar",
    "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango",
    "u": "Uniform", "v": "Victor", "w": "Whiskey", "x": "X-ray",
    "y": "Yankee", "z": "Zulu",
}

DIGIT_WORDS = {
    "en-us": {
        "0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four",
        "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine",
    },
    "da-dk": {
        "0": "Nul", "1": "Et", "2": "To", "3": "Tre", "4": "Fire",
        "5": "Fem", "6": "Seks", "7": "Syv", "8": "Otte", "9": "Ni",
    },
}


class NatoAlphabet(OVOSSkill):

    def _digit_words_for(self, lang):
        lang = lang.lower()
        return DIGIT_WORDS.get(lang) or DIGIT_WORDS.get("en-us", {})

    def _spell(self, text, lang):
        """Returns a list of NATO words / digit words for each
        letter/digit in `text`, skipping anything else (spaces,
        punctuation) rather than trying to announce them."""
        digit_words = self._digit_words_for(lang)
        words = []
        for char in text:
            lower = char.lower()
            if lower in NATO_WORDS:
                words.append(NATO_WORDS[lower])
            elif lower in digit_words:
                words.append(digit_words[lower])
        return words

    @intent_handler("spell_word.intent")
    def handle_spell_word(self, message):
        text = (message.data.get("word") or "").strip()
        if not text:
            self.speak_dialog("nothing_to_spell")
            return
        words = self._spell(text, self.lang)
        if not words:
            self.speak_dialog("nothing_spellable", {"word": text})
            return
        self.speak_dialog("spelled_word", {"spelled": ", ".join(words)})
