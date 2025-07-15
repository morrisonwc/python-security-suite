# caesar-cipher.py
#     This program will take a user's file
#     and encrypt or decrypt the input of a
#     caesar cipher. 
# Programmed by: W. Cale

def encrypt(file_name, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = "!?.,' \n"
    
    if ("encrypted-" + file_name == False):
        open("encrypted-" + file_name, "x")
    else:
        encrypted_file = open("encrypted-" + file_name, "w")
    
    user_file = open(file_name, "r")
    file_text = user_file.read()
    
    for char in file_text.lower():
        if (char in punctuation):
            encrypted_file.write(char)
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_file.write(alphabet[new_index])

    encrypted_file.close()
    user_file.close()

def decrypt(file_name, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = "!?.,' \n"
    
    if ("decrypted-" + file_name == False):
        open("decrypted-" + file_name, "x")
    else:
        decrypted_file = open("decrypted-" + file_name, "w")
    
    user_file = open(file_name, "r")
    file_text = user_file.read()
    
    for char in file_text.lower():
        if (char in punctuation):
            decrypted_file.write(char)
        else:
            index = alphabet.find(char)
            new_index = (index - offset) % len(alphabet)
            decrypted_file.write(alphabet[new_index])

    decrypted_file.close()
    user_file.close()

def main():
    print("This program encrypts and decrypts files ")
    print("using a Caesar Cipher.\n")

    while True:
        print("The following options are available:")
        print("1. Encrypt file")
        print("2. Decrypt file")
        print("3. Exit program\n")
        user_menu = int(input("Please choose one of the above: "))

        if (user_menu == 1):
            user_file = input("Please enter a file to encode: ")
            user_offset = int(input("Please enter a key (integer): "))
            
            encrypt(user_file, user_offset)
            print("File encrypted.\n")

        elif (user_menu == 2):
            user_file = input("Please enter a file to decode: ")
            user_offset = int(input("Please enter a key (integer): "))
            
            decrypt(user_file, user_offset)
            print("File decrypted.\n")

        elif (user_menu == 3):
            print("Thank you for using my Caesar Cipher.")
            break

        else:
            print("Please choose a valid option.\n")
            continue

main()
