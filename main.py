import crypter
import time

while True:
    print()
    print("Menù".center(50))
    print("\nOptions:\n")
    print("[1] Encrypt a sentence")
    print("[2] Decrypt a sentence\n")
    print("[3] Encrypt a file")
    print("[4] Decrypt a file\n")
    print("[5] Stop the code\n")
    var = str(input("Chose One Option > "))
    print()
    if var == "1":
        print("Encrypt a sentence".center(50))
        sentence = input("Write the sentence > ")
        key = input("Write the encryption key > ")
        return_var = crypter.encrypt(key, sentence)
        print(f"[LOG] Encrypted Phrase: {return_var}")
        print("You will be returned to the menu in 10 seconds")
        time.sleep(10)
    elif var == "2":
        print("Decrypt a sentence".center(50))
        sentence = input("Write the sentence > ")
        key = input("Write the encryption key > ")
        return_var = crypter.decrypt(key, sentence)
        print(f"[LOG] Decrypted Phrase: {return_var}")
        print("You will be returned to the menu in 10 seconds")
        time.sleep(10)
    # - File
    elif var == "3":
        print("Encrypt a file".center(50))
        sentence = input("File name / file path > ")
        key = input("Write the encryption key > ")
        crypter.file_encrypt(key, sentence)
        print("You will be returned to the menu in 5 seconds")
        time.sleep(5)
    elif var == "4":
        print("Decrypt a file".center(50))
        sentence = input("File name / file path > ")
        key = input("Write the encryption key > ")
        return_var = crypter.file_decrypt(key, sentence)
        print("You will be returned to the menu in 5 seconds")
        time.sleep(5)
    # - Stop
    elif var == "5":
        exit()
