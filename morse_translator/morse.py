from datetime import datetime

from pydub import AudioSegment


class EncodedMorse:
    def __init__(self, code: str):
        self.code = code

    def save(self, path: str) -> None:
        """Saves the audio to a specified path."""

        dot = AudioSegment.from_wav(".\\morse_translator\\sounds\\dot.wav")
        dash = AudioSegment.from_wav(".\\morse_translator\\sounds\\dash.wav")
        silence = AudioSegment.from_wav(".\\morse_translator\\sounds\\silent.wav")
        starting_audio: AudioSegment = AudioSegment.from_wav(".\\morse_translator\\sounds\\starting_audio.wav") 

        for i in self.code:
            if i == ".":
                starting_audio += dot
            elif i == "-":
                starting_audio += dash
            else:
                starting_audio += silence

        starting_audio.export(path, format="mp3")


class DecodedMorse:
    def __init__(self, text: str) -> None:
        self.text = text
