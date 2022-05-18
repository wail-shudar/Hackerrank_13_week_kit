#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
def pylons(k, arr):
    count = i = 1
    try: i = (k-1) - arr[k-1::-1].index(1)
    except Exception: return -1
    while i < len(arr)-k:        
        prev = count 
        for j in reversed(range(i+1, min(i+k*2, len(arr)))):
            if arr[j]: count +=1; i = j; break        
        if prev==count: return -1       
    return count

# alt. solution by https://www.hackerrank.com/profile/noaht1
# def pylons(k, arr):
#     count=0
#     prevpos=-1
#     pos=k-1
#     while pos<len(arr)+k-1:
#         while pos>=len(arr) or (arr[pos]==0 and prevpos<pos):
#             pos-=1
#         if prevpos==pos:
#             print(pos)
#             return -1
#         prevpos=pos
#         count+=1
#         pos+=(2*k-1)
#     return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
