#Completed by: Wa'il Shudar

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    OFFSET = 96
    curLetter = ''
    weights = set()
    
    for letter in s:
        if curLetter and letter != curLetter[0]:
            curLetter = ''
        
        curLetter += letter 
        weights.add((ord(letter) - OFFSET) * len(curLetter))

    return ['Yes' if q in weights else 'No' for q in queries]

# partial solution failing some tests. Not sure why.
# def weightedUniformStrings(s, queries):
    
#     w, count = set(), Counter(s) 
#     for c in set(s):
#         [w.add((ord(c)-96)*i) for i in range(1, count[c]+1)]
#     print(count)
#     return ['Yes' if q in w else 'No' for q in queries]



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
