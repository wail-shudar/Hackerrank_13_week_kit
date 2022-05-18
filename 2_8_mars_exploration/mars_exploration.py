#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # constraints    
    if not (1 <= len(s) and len(s) <= 99):
        raise Exception('length')
    
    elif (len(s) % 3) != 0:
        raise Exception('modulo')
    
    elif re.search('[^A-Z]', s):
        raise Exception('value') 
           
    else:
        
        return sum(s[i] != 'SOS'[i % 3] for i in range(0, len(s)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
