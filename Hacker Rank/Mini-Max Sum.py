import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    lastIndex = len(arr)-1
    minSum = 0
    maxSum =0
    for i in range(4):
        minSum += arr[i]
        maxSum += arr[lastIndex]
        lastIndex -=1
    print(minSum, maxSum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
