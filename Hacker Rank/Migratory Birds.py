import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count =[]
    maxB = None
    ID=1
    for i in range(1,6):
        count.append(arr.count(i))
    for i in range(5):
        if maxB is None:
            maxB=count[i]
        else:
            if count[i]>maxB:
                maxB=count[i]
                ID=i+1
    return ID
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
