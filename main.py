from datetime import datetime

from morse_translator import Translator

print("-" * 50)
print("Morse Code Translator")
print("Made by Jedddy")
print("-" * 50)

t = Translator()

while True: 

    _type = input('[1] Encode Morse from Text\n[2] Decode Morse\n')

    if _type == "1":
        text = input("Input your text: ")
        translated = t.encode(text)

        prompt = input("Save to audio file? [Y/N]: ").lower()

        if prompt == "y":
            translated.save(f"{int(datetime.now().timestamp())}.mp3")

        choice = input("Translate another one? [Y/N]: \n" + "-" * 50 + "\n").lower()
        if choice != "y":
            print("Thank you for using my translator!")
            break

    elif _type == "2":
        morse = input("Input your morse code: ")
        print(t.decode(morse).text)
        choice = input("Translate another one? [Y/N]\n" + "-" * 50 + "\n").lower()
        if choice != "y":
            print("Thank you for using my translator!")
            break

    else:
        print("Not a valid answer.")
