#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # constraints
    if not (0 < len(s) and len(s) <= 10**3):
        exit(1)
    if re.search('[^a-zA-Z\s]', s):
        exit(1)
    
    s = s.lower().replace(' ', '')
    return 'pangram' if len(set(s)) == 26 else 'not pangram'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
