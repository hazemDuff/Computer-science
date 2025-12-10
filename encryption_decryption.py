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
#string, binary, and HexaDecimal conversions
################################################################################################

def strToBin(string): #a simple function that converts the inputed string to a binary number
    result = ''
    for i in string: #loop through each character in the string
        result += format(ord(i), '08b') #use ACSII code to convert each character to an 8-bit binary number and appends that to the result
    if len(result) < 64: #if the binary number is longer than 64 bits
        result += ('0' * (64 - len(result))) #add 0s until the number is exactly 64 bits
    else:
        result = result[:64] #else if the number is greater than or equal to 64 bits, take the first 64 bits. This ensures that the binary number is exactly 64 bits
    return result

def binToStr(binary): #a simple function that convert binary numbers to string
    result = ''
    for i in range(0, len(binary), 8): #loop through our binary number in increments of 8
        byte = binary[i:i+8] #slice the binary numbers in groups of 8 as each 8 bits represent 1 character
        result += chr(int(byte, 2)) #convert the byte(8-bits) to a character and append to result forming our word
    return result

def binTOHex(binaryString): #functiom that converts binary to HexaDecimal
    return format(int(binaryString, 2), 'X')

def hexToBin(hexString): #function that converts HexaDecimal to binary
    return bin(int(hexString, 16))[2:].zfill(len(hexString) * 4)


################################################################################################
#encryption and decryption functions
################################################################################################

def encrypt_text(text, key): #function that breaks our text into 64-bit block so we can encrypt each block
    text = padText(text) #pad our so that its a multiple of 8
    key_bin = strToBin(key[:8]) #converts the first 8 characters of the key to binary
    cipher = ''
    for i in range(0, len(text), 8): #loop through the padded text 64-bits(8 bytes) at a time
        block = text[i:i+8] #slice the text into blocks of 8 bytes/charcters
        block_bin = strToBin(block) #convert 8 bytes to 64-bits
        cipher += DES(block_bin, key_bin, 'encrypt') #encrypt each 64-bit parts of the text using the 'DES' function and append to 'cipher' as a string
    return cipher

def decrypt_text(cipherHex, key): 
    cipherBin = hexToBin(cipherHex)
    keyBin = strToBin(key[:8]) #converts the first 8 characters of the jey to binary
    text = ''
    for i in range(0, len(cipherBin), 64): #loop through the ciphertext 64-bits(8 bytes) at a time
        block_bin = cipherBin[i:i+64] #slice the ciphertext into block of 64 bits
        text += binToStr(DES(block_bin, keyBin, 'decrypt')) #apply the DES algorithm in 'decrypt' mode to the 64 bits and convert the reult to string and append to 'text'
    return unpadText(text) #unpadd the text from the padding applied to it and return it 