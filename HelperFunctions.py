ip = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

fp = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

e = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

p = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

pc1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

pc2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

sbox = [
    # S1
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    # S2
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],
    # S3
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],
    # S4
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],
    # S5
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    # S6
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],
    # S7
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    # S8
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
]

shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

################################################################################################
#Helper functions used in other important functions
################################################################################################

def permute(block, table): #this function is used to shuffel a string of bits 'block' using a specific table 'table'. For example scrambeling our key bits 'block' into pc2 'table'
    result = ''
    for i in table:
        result += block[i - 1]
    return result

def leftShift(bits, n): #this function takes the bits 'bits' and applies the current round's shift to it 'n'
    for i in range(n): #n is 1 or 2 depending on the round
        first = bits[0]
        bits = bits[1:] + first #shift the first bit to the last position to make the left shift
    return bits

def xor(a, b): #created an xor function
    result = ''
    for i in range(len(a)): #compare each bit in the binary numbers 
        if a[i] == b[i]: #if both bits are the same then append '0' to the result
            result += '0'
        else: #if they are not the same append '1' to the result
            result += '1'
    return result

def sboxSub(bits):
    result = '' 
    for i in range(8): #loop through each of the 8 s-boxs, and the 8 groups of 6-bit binary numbers
        block = bits[i*6:(i+1)*6] #extarct 6-bits at a time from the 48 bits(This is done 8 times for each block(8 * 6 = 48))
        row = int(block[0] + block[5], 2) #obtain integer value of the first and last bits to determine our row
        col = int(block[1:5], 2) #obtain integer value of the middle 4 bits to determine our column
        val = sbox[i][row][col] #plot the column and row in the s box and obtain our integer numbers
        valBin = format(val, '04b') #convert that intger number to a 4-bit binary string      
        result += valBin #append the 4-bit binary string to 'result'
    return result

################################################################################################
#Key sheduling functions
################################################################################################

def generate_subkeys(key64): #function that generates the 16 round subkeys 
    key = permute(key64, pc1) #reorder the key using pc1 dropping the parity bits in the proccess
    C = key[:28] #left half of the new shuffled key
    D = key[28:] #right half of the new shuffled key
    subkeys = [] #empty list that will store all the 16 subkeys
    for shift in shifts: 
        C = leftShift(C, shift) #shift the left side with the amount of shifts required for the specic round
        D = leftShift(D, shift) #shift the right side with the amount of shifts required for the specic round
        subkeys.append(permute(C+D, pc2)) #we then group the right and left side and shuffle it once more with pc2 and finally append it to our 'subkeys' list
    return subkeys

################################################################################################
#main DES functions 
################################################################################################

def feistel(R, K): #function that take the 32bit right side of the plaintext(R) and the 48 bits subkey(K) for each of the 16 rounds
    R_expand = permute(R, e) #expand the 32 bit right side to 48 bits
    temp = xor(R_expand, K) #XOR our expanded right side with the subkey
    result = permute(sboxSub(temp), p) #applies the sbox to the result of the XOR and then applies the permutation to it 
    return result


def DES(block, key, mode='encrypt'): #DES function takes 3 arguments: block is the 64 bitstring, key is our 64bit key we get from user, mode just specifies the mode, it is set to encrypt by defult
    block = permute(block, ip) #shuffle our 64-bit block with the initial permutation
    L = block[:32] #left half of the block(32-bits)
    R = block[32:] #right half of the block(32-bits)
    subkeys = generate_subkeys(key) #genrate the 16 subkeys from the 'generate_subkeys' function we created
    if mode == 'decrypt': #if we are decrypting
        subkeys = subkeys[::-1] #reverse the order of the subkeys(k16-k15...-k1)
    for k in subkeys:
        new_L = R #new left becomes our previous round's right
        new_R = xor(L, feistel(R,k)) #new right becomes the XOR between our previous left and the result from the 'feistel' function
        L = new_L #update our left side
        R = new_R #update our right side
    return permute(R+L, fp) #after 16 rounds concatinate both sides and apply the final permutation



