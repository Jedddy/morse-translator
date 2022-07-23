import json
import datetime
import os
from pydub import AudioSegment


"""Open json file and convert into a python dict"""
with open("./utils/json/morse_to_text.json", "r") as text:
    text = json.load(text)

with open("./utils/json/text_to_morse.json", "r") as morse:
    morse = json.load(morse)

def encrypt_text(texts):
    """Encrypt Text
    
    Remove whitespaces from text
    """

    
    texts = " ".join(texts.split())

    msg = ""
    
    """Loop over the string and check if it matches any dict key
    and add the value to the msg variable if it does match and return the text if it doesn't match anything from the di.
    """
    for text in texts.upper():
        if text in morse.keys():
            msg += morse.get(text) + " "
        else:
            msg += text
    
    return msg


def decrypt_text(codes):
    """Decrypting Morse Code
    
    Splitting the input by spaces
    """

    codes = codes.split()

    msg = ""

    """Loop over the list returned by the split function and check if it matches any dict key
    and add the value to the msg variable if it does match and return "#" if the character is not a morse code.
    """
    for code in codes:
        if code in text.keys():
            msg += text[code]
        else:
            msg += "#"
    
    return msg


def save_to_file(texts, morse=False):
    date = datetime.datetime.now()

    formatted_date = date.strftime("%b %d, %Y - %H:%M:%S")
    
    if morse:
        with open("logs.txt", "a") as f:
            f.write(f"Type: Morse-To-Text at {formatted_date}\nValue: {texts}\n" + "-" * 50 + "\n")
    else:
        with open("logs.txt", "a") as f:
            f.write(f"Type: Text-To-Morse at {formatted_date}\nValue: {texts}\n" + "-" * 50 + "\n")


def save_audio(folder, audio_file):
    date = datetime.datetime.now()
    formatted_date = date.strftime("%Y_%d_%H_%M_%S") #Adding Date Values to the sound file so we wont overwrite a soundfile for having the same name
    file = audio_file.export(f"./{folder}/exported_morse{formatted_date}.wav")
    
    return file


def encode():
    text = input("Input Text: ")

    encrypted = encrypt_text(text)

    print("-" * 50 + "\nTranslated text: " + encrypted + "\n"+ "-" * 50)
    save_to_file(encrypted)
    print("Saved into logs.txt")
    print("-" * 50)

    save = input("Do you want to save Audio file? [Y/N]: ").lower()
    print("-" * 50)
    if save == "y":
        dot = AudioSegment.from_wav("./utils/sounds/dot.wav")
        dash = AudioSegment.from_wav("./utils//sounds/dash.wav")
        silence = AudioSegment.from_wav("./utils/sounds/silent.wav")
        starting_audio = AudioSegment.from_wav("./utils/sounds/starting_audio.wav") 

        """Loop over the morse code and concatenate audios matching the elements of the morse code."""

        for i in encrypted:
            if i == ".":
                starting_audio += dot
            elif i == "-":
                starting_audio += dash
            elif i == " " or "/":
                starting_audio += silence
        
        try:
            folder = "exported_sounds"
            audio = save_audio(folder, starting_audio)
            print(f"Audio file saved as: {audio.name[18:]}")
        except FileNotFoundError:
            os.mkdir("exported_sounds")
            folder = "exported_sounds"
            audio = save_audio(folder, starting_audio)
            print(f"Audio file saved as: {audio.name[18:]}")
    elif save == "n":
        pass


def decode():

    text = input("Input Morse Code: ")

    decrypted = decrypt_text(text)

    print("-" * 50 + "\nDecoded Morse Code: " + decrypted + "\n" + "-" * 50)
    save_to_file(decrypted, morse=True)
    print("Saved into logs.txt")
    print("-" * 50)
    