import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Completed by: Wail Shudar
    if len(n) == 1: return n 
    else:
        n = reduce(lambda x,y: int(x)+int(y), n)
        return superDigit(str(n*k), 1)

    # alt solution by: noaht1@HackerRank
    # return (int(n)*k-1)%9+1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(superDigit())
