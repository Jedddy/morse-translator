from utils.utils import encode, decode

print("-" * 50)
print("Morse Code Translator")
print("Made by Jedddy")
print("-" * 50)


while True: 
    
    _type = input('[1] Encode Morse from Text\n[2] Decode Morse\n')

    if _type == "1":
        encode()
        choice = input("Translate another one? [Y/N]: \n" + "-" * 50 + "\n").lower()
        if choice != "y":
            print("Thank you for using my translator!")
            break

    elif _type == "2":
        
        decode()

        choice = input("Translate another one? [Y/N]\n" + "-" * 50 + "\n").lower()
        if choice != "y":
            print("Thank you for using my translator!")
            break

    else:
        print("Not a valid answer.")