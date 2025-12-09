from HelperFunctions import permute, e, xor, sboxSub, p, DES


################################################################################################
#padding and unpadding functions to make code accept strings of any legnth
################################################################################################

def padText(text): #this pads the text and lets us input strings that are greater than 8 characters
    pad_len = 8 - (len(text) % 8) #checks how many padding bytes we need to make the number of characters in the string a multiple of 8
    return text + chr(pad_len) * pad_len #adds the padding which leaves us with a string legth that is a multiple of 8 so that we do the DES alogorith on each 8 characters in one time

def unpadText(text): #funtion that removes the padding that we did 
    pad_len = ord(text[-1]) #convert the last character to a number so that we know how much padding was added
    return text[:-pad_len] #remove all the padding we added

################################################################################################
#string to binary conversions
################################################################################################

def strToBin(string): #a simple function that converts the inputed string to a binary number
    result = ''
    for i in string: #loop through each character in the string
        result += format(ord(i), '08b') #use ACSII code to convert each character to an 8-bit binary number and appends that to the result
    return result.ljust(64, '0')[:64]

def binToStr(binary): #a simple function that convert binary numbers to string
    result = ''
    for i in range(0, len(binary), 8): #loop through our binary number in increments of 8
        byte = binary[i:i+8] #slice the binary numbers in groups of 8 as each 8 bits represent 1 character
        result += chr(int(byte, 2)) #convert the byte(8-bits) to a charachter and appent to result forming our word
    return result

################################################################################################
#encryption and decryption functions
################################################################################################

def encrypt_text(text, key):
    text = padText(text)
    key_bin = strToBin(key[:8])
    cipher = ''
    for i in range(0, len(text), 8):
        block = text[i:i+8]
        block_bin = strToBin(block)
        cipher += DES(block_bin, key_bin, 'encrypt')
    return cipher

def decrypt_text(cipher_bin, key):
    key_bin = strToBin(key[:8])
    text = ''
    for i in range(0, len(cipher_bin), 64):
        block_bin = cipher_bin[i:i+64]
        text += binToStr(DES(block_bin, key_bin, 'decrypt'))
    return unpadText(text)