# Completed by Wail Shudar   

import math
import os
import random
import re
import sys
from copy import deepcopy
#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def detonate(grid):
    _grid = [list('O'*len(grid[0])) for _ in range(len(grid))] 
    
    for i in range(len(grid)): # row selector
        for j in range(len(grid[0])): # row traverser
            if grid[i][j] == 'O': # marks space around bombs       
                for y, x in zip([i, i+1, i-1, i, i], [j, j, j, j+1, j-1]):      
                    try: _grid[abs(y)][abs(x)] = '.' # abs() avoids wraparound
                    except Exception: pass            
    return [''.join(row) for row in _grid] # list to str

    
def bomberMan(n, grid): 
    if n == 1: return grid 
    elif not n%2: return ['O'*len(grid[0])]*len(grid)
    else:       
        return detonate(grid) if (n-1)%4 else detonate(detonate(grid))
       
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
