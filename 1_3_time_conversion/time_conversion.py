import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # completed by: Wail Shudar
    s_list = s.split(':', 2)    

    if s_list[2][-2:] == 'AM':
        if s_list[0] == '12':
            s_list[0] = '00'
    elif s_list[2][-2:] == 'PM':
        s_list[0] = int(s_list[0])
        if s_list[0] < 12:
            s_list[0]+=12

    converted = ':'.join(str(_) for _ in s_list)[:-2]
    return str(converted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
