import json
import datetime

from .morse import EncodedMorse, DecodedMorse


with open(".\\morse_translator\\json\\morse_to_text.json", "r") as text:
    text: dict = json.load(text)

with open(".\\morse_translator\\json\\text_to_morse.json", "r") as morse:
    morse: dict = json.load(morse)


class Translator:
    def __init__(self, log: bool = True) -> None:
        self.log = log

    def encode(self, text: str) -> EncodedMorse:
        """Encodes a message into morse code."""

        encoded = " ".join([morse.get(t, "#") for t in text.strip().upper()])
        self._log(encoded)
        return EncodedMorse(encoded)

    def decode(self, code: str) -> DecodedMorse:
        """Decodes morse text."""

        decoded = "".join([text.get(morse, "#") for morse in code.strip().split()])
        self._log(decoded, morse=True)
        return DecodedMorse(decoded)

    def _log(self, texts: str, morse: bool = False) -> None:
        date = datetime.datetime.now()
        formatted_date = date.strftime("%b %d, %Y - %H:%M:%S")

        with open("morse_logs.txt", "a") as f:
            if morse:
                f.write(f"Type: Morse-To-Text at {formatted_date}\nValue: {texts}\n" + "-" * 50 + "\n")
            else:
                f.write(f"Type: Text-To-Morse at {formatted_date}\nValue: {texts}\n" + "-" * 50 + "\n")
