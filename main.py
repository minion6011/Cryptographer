import sys
sys.dont_write_bytecode = True
import crypter

run = True

while run:
    print()
    print("<--------------- Menù --------------->")
    print("\nOptions:\n")
    print(">>> [1] Encrypt a sentence")
    print(">>> [2] Decrypt a sentence")
    print(">>> [3] Encrypt a file")
    print(">>> [4] Decrypt a file")
    print(">>> [5] Stop the code")
    print("\n<------------------------------------>\n")
    var = str(input("Chose One Option > "))
    print()
    if var == "1":
        print(" > Encrypt a sentence")

        sentence = input("Write the sentence > ")
        key = input("Write the encryption key > ")
        return_var = crypter.encrypt(key, sentence)
        
        print(f"Encrypted Phrase: {return_var}")
        print("Press [ENTER] to continue")
        input()
    elif var == "2":
        print(" > Decrypt a sentence")

        sentence = input("Write the encrypted sentence > ")
        key = input("Write the encryption key > ")
        return_var = crypter.decrypt(key, sentence)

        print(f"Decrypted Phrase: {return_var}")
        print("Press [ENTER] to continue")
        input()
    # - File
    elif var == "3":
        print(" > Encrypt a file")

        sentence = input("File name / file path > ")
        key = input("Write the encryption key > ")
        crypter.file_encrypt(key, sentence)

        print("Press [ENTER] to continue")
        input()
    elif var == "4":
        print(" > Decrypt a file")

        sentence = input("File name / file path > ")
        key = input("Write the encryption key > ")
        crypter.file_decrypt(key, sentence)

        print("Press [ENTER] to continue")
        input()
    # - Stop
    elif var == "5":
        run = False
    else:
        print(" > Invalid Option")
