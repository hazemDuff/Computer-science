from HelperFunctions import pc1, pc2, leftShift, permute, shifts

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
