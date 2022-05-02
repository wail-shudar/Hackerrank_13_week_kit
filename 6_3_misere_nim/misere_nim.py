import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):
    # completed by: Wail Shudar
    balanced = reduce(lambda i,j: i^j, s)
    singles = (1 in set(s)) and (len(set(s))==1)
    even = len(s)%2==0
    
    if (even and singles) or (not singles and balanced):
        return 'First'
    else: return 'Second'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
