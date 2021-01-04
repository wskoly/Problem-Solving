import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        j=0
        while(j<(n-(i+1))):
            print(' ', end='')
            j+=1
        for k in range(i+1):
            print('#', end='')
        print('')

if __name__ == '__main__':
    n = int(input())

    staircase(n)
