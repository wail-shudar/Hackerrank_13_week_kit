import math
import os
import random
import re
import sys
from math import log2, floor
#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Completed by: Wail Shudar
    turn = 1
    
    while n > 1:
        if (n & (n-1))==0: n //= 2
        else: n-= int(2**floor(log2))
        turn += 1
        
    return 'Richard'if turn%2 else 'Louise'

    # alt solution by: ababh@HackerRank
    # n |= n - 1
    # c = False
    # while n:
    #     n &= n - 1
    #     c = not c
    # if c:
    #     return 'Richard'
    # return 'Louise'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)
        print(result, '\n')
    #     fptr.write(result + '\n')

    # fptr.close()
