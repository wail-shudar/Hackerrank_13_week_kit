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


def countSort(arr):
    # completed by: Wail Shudar
    ans = [[]]
    
    for i in range(len(arr)):
        if i < len(arr)//2: arr[i][1] = '-'     
        if len(ans) <= int(arr[i][0]): 
            [ans.append([]) for _ in range(int(arr[i][0]))]         
        ans[int(arr[i][0])].append(arr[i][1])

    
    print(' '.join(sum(ans, [])))
    logger.debug('%s seconds', ('%.6f'%(time.time()-st)))
   
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)

