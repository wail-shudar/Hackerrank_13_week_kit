#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # constraints
    if not (2 <= steps and steps <= 10**6 and steps == len(path)):
        exit(1)
        
    if re.search('[^DU]', path):
        exit(1)
    
    # variables
    altitude = valley_count = 0
    in_valley = False  
    
    # FSM logic
    for step in path:
        altitude += 1 if step == 'U' else -1                 

        if in_valley:
            if altitude == 0:
                in_valley = False  
                                
        elif not in_valley:
            if altitude == -1:             
                in_valley = True
                valley_count += 1
        
    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
