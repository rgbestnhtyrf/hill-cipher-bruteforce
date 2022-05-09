from itertools import product
import numpy as np

def apply_cipher_decode(cipher, key, block_size):
    result = []
    for i in range(len(cipher)//block_size):
        mul = np.matmul(key,cipher[block_size*i:block_size*i+block_size])
        result.append(chr((mul[0]%26)+97))
        result.append(chr((mul[1]%26)+97))

    return result

def getChArrToString(arr):
    result = ""
    for ch in arr:
        result += ch

    return result


def hill():
    input = "HMECIAFGJNFBLJ"
    input = input.lower()

    inputToNum = []
    for char in input:
        inputToNum.append(ord(char) - 97)

    n, m = 2, 2

    x = product(range(26), repeat=n*m)
    x = np.reshape(list(x), (-1, n, m))


    for a in list(x):
        print(getChArrToString(apply_cipher_decode(inputToNum,a,2)))
    


            
hill()



