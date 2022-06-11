#!/bin/python3
# Completed by: Wa'il Shudar
import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    lengths = [0]
    
    for c_tup in combinations(set(s), 2):    
        c_arr, l = [c for c in s if c in c_tup], 1
        
        for i in range(1,len(c_arr)): 
            if c_arr[i] != c_arr[i-1]: l+=1
            else: l=0; break
            
        lengths.append(l)
        
    return max(lengths)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
