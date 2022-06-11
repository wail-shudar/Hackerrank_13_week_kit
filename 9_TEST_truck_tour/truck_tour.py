# Completed by: Wa'il Shudar

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    l, net_gas = len(petrolpumps), [p[0]-p[1] for p in petrolpumps]
    
    for i in range(l):
        curr_gas = 0
        for j in range(i, l+i):
            curr_gas += net_gas[j%l]
            if curr_gas < 0: break
            elif j+1==l+i: return i
    return None

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
