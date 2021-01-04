import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(' ','')
    length = len(s)
    row = math.floor(math.sqrt(length))
    col = math.ceil(math.sqrt(length))
    if row*col<length:
        row+=1
    slist = []
    sIndex = 0
    for i in range(row):
        slist.append(s[sIndex:(sIndex+col)])
        sIndex+=col
    encStr=''
    for i in range(col):
        for j in range(row):
            try:
                encStr+=slist[j][i]
            except:
                break
        if(i==col-1):
            continue
        encStr+=' '
    return encStr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
