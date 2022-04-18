# https://www.hackerrank.com/profile/maria_schoenhol1

import math
import os
import random
import re
import sys
import time
import logging
st=time.time()
logging.basicConfig(level=logging.NOTSET)
logger=logging.getLogger() 

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    for i in range(len(arr)//2):
        arr[i][1] = '-'
    sorted_str = [v for k, v in sorted(arr, key=lambda pair: int(pair[0]))]
    print(' '.join(sorted_str))
    logger.debug('%s seconds', ('%.6f'%(time.time()-st)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
