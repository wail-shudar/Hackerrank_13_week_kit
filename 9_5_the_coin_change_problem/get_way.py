# Completed by: Wa'il Shudar

import math
import os
import random
import re
import sys
from itertools import combinations_with_replacement

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
def getWays(n, c):
    rec = [1]+[0]*n    
    for x in c:
        for i in range(x, n+1):
            rec[i] += rec[i-x]
    return rec[n]
    
# First attempt, fails due to time complexity
# def getWays(n, c):
#     c, ans = sorted([x for x in c if x <= n]), []
    
#     for i in range(1, (n//min(c))+1):
#         if i ==1:
#             pass
#         for p in combinations_with_replacement(c, r=i):   

#             if sum(p)==n: ans.append(p)
#             elif len(set(p))==1 and sum(p)> n: break
            
#     return len(ans)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    print(ways)
    # fptr.write(str(ways) + '\n')

    # fptr.close()


