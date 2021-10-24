# EJERCICIO 12

# Participante:
# Jose Luis Hernandez Meza

# Import of modules
import argparse
import time
import os
import DetectEs

# Start argparse
parser = argparse.ArgumentParser(
    description = "Cesar Encryption Tool"
    )

# We add the required arguments
parser.add_argument(
    "-mode",
    nargs = "?",
    default = "e",
    type = str, 
    help = "Type the working mode: 'e' for encrypt, 'd' for decrypt or 'c' for crack message.")
parser.add_argument(
    "-message",
    nargs = "?",
    default = "Soy LSTI y me gusta programar",
    type = str, 
    help = "Type the message to use")
parser.add_argument(
    "-key",
    nargs = "?",
    default = "clave del dia",
    type = str, 
    help = "Type the message to use")

args = parser.parse_args()

# We make the arguments simpler
mod = args.mode
message = args.message
key = len(args.key)

print("==============================")
print("-------STARTING PROGRAM-------")
print("==============================")

time.sleep(2)

# We define our dictionary
dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# Create the function that encrypts all messages
def Encrypt(message, key):
    translated = '' # We have an empty dictionary
    for symbol in message:
        if symbol in dict:
            symbolIndex = dict.find(symbol)
            translatedIndex = symbolIndex + key
            if translatedIndex >= len(dict):
                translatedIndex = translatedIndex - len(dict)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(dict)
            
            translated = translated + dict[translatedIndex]
        else:
            translated = translated + symbol
    print(translated)

# Create the function that will decrypt all messages
def Decrypt(message, key):
    translated = '' # We have an empty dictionary
    for symbol in message:
        if symbol in dict:
            symbolIndex = dict.find(symbol)
            translatedIndex = symbolIndex - key
            if translatedIndex >= len(dict):
                translatedIndex = translatedIndex - len(dict)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(dict)
            translated = translated + dict[translatedIndex]
        else:
            translated = translated + symbol
    print(translated)

# We create the function that will crack all messages using brute force
def Crack(message, key):
    for key in range(len(dict)):
        translated = '' # We have an empty dictionary
        for symbol in message:
            if symbol in dict:
                symbolIndex = dict.find(symbol)
                translatedIndex = symbolIndex - key
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(dict)
                translated = translated + dict[translatedIndex]
            else:
                translated = translated + symbol
        print('Key #%s: %s' % (key, translated))

if __name__ == "__main__":
    # Verify the selected mode
    if mod == "e":
        print("You have selected the message encryption option")
        message = message.upper()
        print("Your encrypted message is:")
        Fraenc = Encrypt(message, key) # Print encrypted message
    elif mod == "d":
        print("You have selected the message decryption option.")
        message = message.upper()
        print("our decrypted message is:")
        Frades = Decrypt(message, key) # Prints the decrypted message
    elif mod == "c":
        print("You have selected the message cracking option")
        message = message.upper()
        print("The cracked message is:")
        Fracrack = Crack(message, key) # Print cracked message
