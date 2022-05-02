import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Completed by: Wail Shudar
    maxl = [0]
    count = len([maxl.append(v) for v in arr if v > maxl[-1]])
    return 'BOB' if count%2 else 'ANDY'

    # py3.8 solution using assignment expression
    # maxi = 0
    # maxl = [maxi := v for v in arr if v > maxi]
    # return 'BOB' if len(maxl)%2 else 'ANDY'


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

    #     fptr.write(result + '\n')

    # fptr.close()
