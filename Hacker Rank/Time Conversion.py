import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hh = int(s[:2])
    mm = s[3:5]
    ss = s[6:8]
    am = s[8:10]
    if hh < 12 and am == 'PM':
        hh += 12
    elif hh == 12 and am == 'AM':
        hh = 0
    if hh<10:
        hh = '0'+str(hh)
    else:
        hh = str(hh)
    time = hh+':'+mm+':'+ss
    return time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
