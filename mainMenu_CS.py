from encryption_decryption import encrypt_text, decrypt_text
def mainMenu1(): #main menu 1, more complex, and asks the user more questions
    while True:
        print("\n-----------DES Encryption algorithm-----------")
        choice = int(input("Do you want to encrypt(1) or decrypt(2) or exit(3):"))
        if choice == 1:
            plaintxt = input("Enter text to encrypt:")
            key = input("Enter your key:")
            resultCipher = encrypt_text(plaintxt, key)
            print(f"your encrypted text in binary: {resultCipher}")
            print(f"your encrypted text in Hexa-Decimal: {hex(int(resultCipher,2))[2:].upper()}") #convert the binary number to HexaDecimal

        elif choice == 2:
            ciphertxt = input("Enter cipher text you want to decrypt IN HexaDecimal:") #input must be in HexaDecimal 
            keyDec = input("Enter the key:")
            resultPlain = decrypt_text(ciphertxt, keyDec)
            print(f"Decrypted cipher text to plain text: {resultPlain}")

        elif choice == 3:
            print("Thankyou for using my code, goodbye...")
            break
        
        else:
            print("Invalid choice input must be (1-3)")

def mainMenu2(): #main menu 2, simple, asks user only 2 questions and retuns the encrypted and decrypted results in one go
    while True:
        print("\n-----------DES Encryption algorithm-----------")

        plaintxt = input("Enter text to encrypt:")
        key = input("Enter your key:")
        resultCipher = encrypt_text(plaintxt, key)
        resultCipher_hex = hex(int(resultCipher,2))[2:].upper()
        print(f"your encrypted text in binary: {resultCipher}")
        print(f"your encrypted text in Hexa-Decimal: {hex(int(resultCipher,2))[2:].upper()}")

        resultPlain = decrypt_text(resultCipher_hex, key)
        print(f"Decrypted cipher text back to plain text: {resultPlain}")

def testCases():
    pass            
        
if __name__ == "__main__":
    while True:
        choice = int(input("do u want simple main menu(1) or the detailed main menu(2):"))
        if choice == 1:
            mainMenu2()
            break
        elif choice == 2:
            mainMenu1()
            break
        else:
            print("Invalid input")
