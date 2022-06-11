# Completed by: Wa'il Shudar
import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def chiefHopper(arr):
    e = arr[0]//2; passed = False

    while not passed:
        e_sum = e        
        for i in range(len(arr)):
            if e_sum > arr[i]: e_sum += e_sum-arr[i]
            elif e_sum < arr[i]: e_sum -= arr[i]-e_sum
        
            if e_sum < 0: e += 1; break
            elif i+1 == len(arr): passed = True; break
    return e




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
