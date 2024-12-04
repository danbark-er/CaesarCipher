# Script to encrypt or decrypt a message using a caesar cipher
# Author : Dan Barker
# Date created : 21/04/2022
# Last modified : 08/06/2022

# Import modules for time delay and heading
import time
from art import *

# Print the welcome page
heading = text2art("Caesar    Cipher!", font='graffiti', chr_ignore=True)
print("===================================================================================================")
print(heading)
print("===================================================================================================\n")
print("                                       Created by Dan Barker.\n")
print("Welcome. ")

# Get user input - encryption or decryption? | convert input to uppercase | define where start of code is (main)
def main():
    while True:
        x = input("\nPlease type 'E' to encrypt a message or 'D' to decrypt a message : ")
        x = x.upper()
        while x not in ("E", "D"):
            x = input("\n================== Incorrect input ==================\n\n"
                      "Please type 'E' for encryption or 'D' for decryption : ")
            x = x.upper()
# If user input 'E' - Ask what message they want to encrypt? | print error and loop if input is left empty
        if x == "E":
            msg = input("\nWhat message would you like to encrypt? : ")
            while not msg:
                msg = input("\n============== Message cannot be blank! ==============\n\n"
                            "What message would you like to encrypt? : ")
            else:
                break
# If user input 'D' - Ask what message they want to decrypt? | print error and loop if input is left empty
        if x == "D":
            msg = input("\nWhat message would you like to decrypt? : ")
            while not msg:
                msg = input("\n============== Message cannot be blank! ==============\n\n"
                            "What message would you like to decrypt? : ")
            else:
                break
# Message conversion | convert to uppercase, replace full stop with 'X', remove special characters and numbers
    msg = msg.upper().replace('.', 'X')
    newmsg = ''.join(sc for sc in msg if sc.isalnum())
    newmsg = ''.join((dig for dig in newmsg if not dig.isdigit()))
# Message will return blank if no letters were used, in that case print error message and loop back to main
# If the user input is accepted, print it and move one
    while True:
        while not newmsg:
            print("\n================== Incorrect input ==================\n\n"
                  "Please note,\n"
                  "Special characters and numbers will be removed.\n"
                  "Therefore, message must contain letters. Please try again.\n\n"
                  "============================================================= ")
            main()
        else:
            break

    print("\nConverted message : " + newmsg)

# Get user input - shift key | only accept a digit in the range 1-25, loop if else
# Print error message if number is out of range or any other character that isn't a number was used
    while True:
        try:
            shift = int(input("\nPlease choose a shift key (1-25) : "))
            while shift not in range(1, 26):
                shift = int(input("\n================== Out of range! ==================\n\n"
                                      "Please choose a shift key (1-25) : "))
            else:
                break
        except ValueError as e:
            print("\n================== Incorrect input ==================")

# Message encryption | for each letter in the message, find the position/index in the range 0-25 it is
# Using it's unicode value, shift it forwards as many times as specified by the users shift key
# Replace the initial value with the new unicode value
    if x == "E":
        print("\n================== Encrypting " + str(newmsg) + " Please wait... ================== ")
        time.sleep(3)
        encryption = ""
        for c in newmsg:
            if c.isupper():
                c_unicode = ord(c)
                c_index = ord(c) - ord("A")
                new_index = (c_index + shift) % 26
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
                encryption = encryption + new_character

# Print the encrypted text and shift key used
        print("\nEncrypted Text :", encryption)
        print("Cipher Key :", shift)

# Message decryption | for each letter in the decrypted text, find the position/index in the range 0-25 it is
# Using it's unicode value, shift it backwards as many times as specified by the users shift key
# Replace the initial value with the new unicode value
    if x == "D":
        print("\n================== Decrypting " + str(newmsg) + " Please wait... ================== ")
        time.sleep(3)
        decryption = ""
        for c in newmsg:
            if c.isupper():
                c_unicode = ord(c)
                c_index = ord(c) - ord("A")
                new_index = (c_index - shift) % 26
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
                decryption = decryption + new_character

# Print the decrypted text and shift key used
        print("\nDecrypted Text :", decryption)
        print("Cipher Key :", shift)
# User input to exit
    input("\n\nPress enter to exit")
    exit()

main()