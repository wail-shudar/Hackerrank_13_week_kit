import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # solved by: Wail Shudar
    z = arr.count(0)
    p = sum([True for i in arr if i > 0])
    n = len(arr) - p - z

    return [print('%.6f'%(x/len(arr))) for x in [p, n, z]]
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
