import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Completed by: Wail Shudar
    #edge case
    if sum(arr[1:])==0 or sum(arr[:-1])==0: return 'YES'
    # vars
    hl= len(arr)//2
    ar1, ar2= sum(arr[0:hl]), sum(arr[hl+1:])
    greater = True if ar1 > ar2 else False
    # start from middle
    for i in range(hl):
        if ar1==ar2: 
            return 'YES'
        elif greater:
            ar1 -= arr[hl-i-1]; ar2 += arr[hl-i]
            if ar2 > ar1: break
        else: 
            ar1 += arr[hl+i]; ar2 -= arr[hl+i+1]
            if ar1 > ar2: break
    return 'NO'
    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
