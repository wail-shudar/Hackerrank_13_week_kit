# Completed by: Wa'il Shudar
import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    cnt = Counter(s).values()
    cnt_set = list(set(cnt))
    cnt_freq = list(Counter(cnt).values())

    if len(cnt_set) == 1: return 'YES'
    elif len(cnt_set) == 2:
        return 'YES' if cnt_freq.count(1) \
        and (abs(cnt_set[0]-cnt_set[1])==1 or list(cnt).count(1)==1) \
        else 'NO'
    else:
        return 'NO'

# alt. solution by https://www.hackerrank.com/profile/cvorsanger
# def isValid(s):
#     vals =Counter(Counter(s).values())
#     if len(vals) == 1:
#         return "YES"
#     if len(vals) > 2:
#         return "NO"
#     if 1 in vals.values() and ((max(vals.keys()) - min(vals.keys()) ==1) or vals[min(vals.keys())] ==1):
#         return "YES"
#     else:
#         return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()