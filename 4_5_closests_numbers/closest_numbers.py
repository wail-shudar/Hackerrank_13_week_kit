import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # completed by: Wail Shudar
    a = sorted(arr)
    min_diff = min((abs(a[i]-a[i-1]) for i in range(1, len(a))))
    
    return sum(
        (a[i-1:i+1] for i in range(1, len(a)) 
        if abs(a[i-1]-a[i])==min_diff), []
    )
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
