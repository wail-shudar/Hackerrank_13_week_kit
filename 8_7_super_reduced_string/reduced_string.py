#!/bin/python3
# Completed by: Wa'il Shudar
import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    for i in range(1, len(s)):
        if s[i-1]==s[i]: 
            return superReducedString(s[:i-1] + s[i+1:])
    return s if len(s) else 'Empty String'
 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
