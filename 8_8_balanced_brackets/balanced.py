#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def swapBracket(c):
    return c.replace('(', ')').replace('[', ']').replace('{', '}')

def isBalanced(s):
    ref = []
    for c in s:
        if c in['[', '(', '{']: ref.append(swapBracket(c))
        elif not ref or c != ref.pop(): return 'NO'
    return 'YES' if not ref else 'NO'

# alt solution, though not as robust 
# (would fail tests if they had included '|' or '\')
# def isBalanced(s):
#     ref = []
#     for c in s:
#         if c in['[', '(', '{']: ref.append(c)
#         elif not ref or ord(c)-ord(ref.pop())>2: return 'NO'
#     return 'YES' if not ref else 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)
    #     fptr.write(result + '\n')

    # fptr.close()
