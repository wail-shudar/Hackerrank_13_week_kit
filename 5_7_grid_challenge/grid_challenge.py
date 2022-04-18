import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # completed by: Wail Shudar
    for i, s in enumerate(grid):
        if list(s) != sorted(s): grid[i] = ''.join(sorted(s))
    
    in_order = [True if grid[i][j] <= grid[i+1][j] else False
    for j in range(len(grid[0])) for i in range(len(grid)-1)]
    
    return'YES' if all(in_order) else 'NO'


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        #fptr.write(result + '\n')

    #fptr.close()
