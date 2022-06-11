#!/bin/python3
# Completed by: Wa'il Shudar
import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def maxSubarray(arr):
    sarr, sseq = arr[:1], [v for v in arr if v > 0]

    for i in range(1, len(arr)):  
        sarr.append(max(sarr[i-1]+arr[i], arr[i]))

    return [max(sarr), sum(sseq) if sum(sseq) else max(arr)]

# First attempt, fails time complexity
# def maxSubarray(arr):
#     sub, seq = [i for i in arr if i > 0], max(arr)
    
#     if len(arr) == len(sub): 
#         return[sum(arr), sum(sub)]
#     else:
#         for i in range(1,len(arr)):
#             for j in range(len(arr)-i+1):
#                 if sum(arr[j:j+i]) > seq: 
#                     seq = sum(arr[j:j+i])
                    
#     return[seq, sum(sub) if sum(sub) else max(arr)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
