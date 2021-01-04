import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount=0
    orangeCount=0
    for i in apples:
        if s<=(a+i)<=t:
            appleCount+=1
    for i in oranges:
        if s<=(b+i)<=t:
            orangeCount+=1
    print(appleCount)
    print(orangeCount)
            

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
