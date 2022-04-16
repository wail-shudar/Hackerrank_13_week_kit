import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # completed by: Wail Shudar
    count, regex = 0, ['[a-z]', '[A-Z]', '[0-9]', '\W']    
    for e in regex: count += 1 if not re.search(e, password) else 0
    
    return 6-n if n+count < 6 else count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
