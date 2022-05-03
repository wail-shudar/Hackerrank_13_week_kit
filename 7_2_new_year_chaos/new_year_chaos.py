import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Completed by: Wail Shudar
    r = [q[i]-1 for i in range(len(q)) if q[i]-i-1 <= 2]
    if len(r) < len(q): return print('Too chaotic')
    else: return print(sum(
        [1 for i in range(len(r)) for j in range(max(0, r[i]-1),i) if r[j] > r[i]]
    ))

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

