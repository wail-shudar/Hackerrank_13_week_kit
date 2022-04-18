import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # completed by: Wail Shudar
    try:
        if not arr:
            raise ValueError('empty array')
    except ValueError as e:
        print(e)
    
    min_index = min(range(len(arr)), key=arr.__getitem__)
    max_index= (max(range(len(arr)), key=arr.__getitem__))

    min_sum = sum(arr[:max_index] + arr[max_index+1:])
    max_sum = sum(arr[:min_index] + arr[min_index+1:])

    print(min_sum, max_sum)


        
            
        
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
