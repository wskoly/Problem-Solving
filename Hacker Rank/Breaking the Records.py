import math
import os
import random
import re
import sys

def breakingRecords(scores):
    minimum=None
    maximum=None
    highest = 0
    lowest = 0
    for i in scores:
        if minimum is None:
            minimum = i
            maximum = i
        elif i>maximum:
            maximum = i
            highest+=1
        elif i<minimum:
            minimum = i
            lowest +=1
    return highest,lowest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
