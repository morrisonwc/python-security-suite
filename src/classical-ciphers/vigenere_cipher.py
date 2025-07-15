# vigenere-cipher.py
#     This program will take a user's input
#     and code the input with a 
#     vigenere cipher. 
# Programmed by: W. Cale

def encrypt(file_name, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if ("encrypted-" + file_name == False):
        open("encrypted-" + file_name, "x")
    else:
        encrypted_file = open("encrypted-" + file_name, "w")

    user_file = open(file_name, "r")
    file_text = user_file.read()

    for char in file_text.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            encrypted_file.write(char)
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            encrypted_file.write(alphabet[new_index])
    
    encrypted_file.close()
    user_file.close()
    
def decrypt(file_name, key, direction=-1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    if ("decrypted-" + file_name == False):
        open("decrypted-" + file_name, "x")
    else:
        decrypted_file = open("decrypted-" + file_name, "w")

    user_file = open(file_name, "r")
    file_text = user_file.read()

    for char in file_text.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            decrypted_file.write(char)
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            decrypted_file.write(alphabet[new_index])
    
    decrypted_file.close()
    user_file.close()


def main():
    print("This program encodes and decodes messages ")
    print("using a Vigenere Cipher.\n")

    while True:
        print("The following options are available:")
        print("1. Encode message")
        print("2. Decode message")
        print("3. Exit program\n")
        user_menu = int(input("Please choose one of the above: "))

        if (user_menu == 1):
            user_file = input("Please enter a file to encode: ")
            user_key = input("Please enter a key (string): ")
            
            encrypt(user_file, user_key)
            print("File encrypted.\n")

        elif (user_menu == 2):
            user_file = input("Please enter a file to decode: ")
            user_key = input("Please enter a key (string): ")
            
            decrypt(user_file, user_key)
            print("File decrypted.\n")

        elif (user_menu == 3):
            print("Thank you for using my Vigenere Cipher.")
            break

        else:
            print("Please choose a valid option.\n")
            continue

main()
