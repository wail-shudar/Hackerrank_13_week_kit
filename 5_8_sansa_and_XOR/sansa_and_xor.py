import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    # completed by: Wail Shudar
    return reduce(lambda x,z: x^z, arr[::2]) if len(arr)%2 else 0
    
    # attempt 1: failed tests 5-12 due to time constraint
    # e = []
    # for i in range(0,len(arr)-1):
    #     e.extend(list(accumulate(arr[i:], lambda x, y: x^y))[1:])

    # e.pop(len(arr)-2)
    # return reduce(lambda x, y: x^y, e)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
