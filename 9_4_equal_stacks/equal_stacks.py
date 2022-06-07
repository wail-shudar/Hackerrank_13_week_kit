#!/bin/python3
# Completed by: Wa'il Shudar
import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    cyl = [sum(h) for h in [h1, h2, h3]]
    
    while len(set(cyl)) != 1:        
        idx = cyl.index(max(cyl))
        cyl[idx] -= ([h1, h2, h3][idx]).pop(0)
    return cyl[0]
           
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
