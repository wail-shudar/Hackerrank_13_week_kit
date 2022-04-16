import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Completed by: Wail Shudar
    b = list(set(a))
    
    if len(b) == 1:
        return a.count(b[0])
    else:
        return max([
            a.count(b[i-1]) + a.count(b[i]) 
            if abs(b[i-1] - b[i]) <= 1 
            else a.count(b[i-1]) 
            for i in range(1, len(b))    
        ])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
