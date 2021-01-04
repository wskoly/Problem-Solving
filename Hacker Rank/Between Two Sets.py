import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    lowerVal = a[n-1]
    upperVal = b[0]
    ar = []
    count = 0
    for i in range(lowerVal, upperVal+1):
        flag = 0
        for j in range(n):
            if(i%a[j])== 0:
                flag +=1
        if flag == n:
            ar.append(i)
    for i in ar:
        flag = 0
        for j in range(m):
            if(b[j]%i) == 0:
                flag +=1
        if flag == m:
            count +=1
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
