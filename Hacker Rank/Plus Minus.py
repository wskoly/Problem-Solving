import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i>0:
            positive += 1
        elif i<0:
            negative += 1
        else:
            zero += 1
    positive = float(positive/len(arr))
    negative = float(negative/len(arr))
    zero = float(zero/len(arr))
    print("{0:.6f}\n{1:.6f}\n{2:.6f}".format(positive,negative,zero))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
