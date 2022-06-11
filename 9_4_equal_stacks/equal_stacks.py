#!/bin/python3
# Completed by: Wa'il Shudar
import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    cyl = [sum(h) for h in [h1, h2, h3]]
    
    while len(set(cyl)) != 1:        
        idx = cyl.index(max(cyl))
        cyl[idx] -= ([h1, h2, h3][idx]).pop(0)
    return cyl[0]
           
# first attempt. I misunderstood that stacks can be removed  
# from any position in the cylinder as opposed to from the top. 
# A more involved problem.

# from itertools import combinations
# def equalStacks(h1, h2, h3):
#     stacks = [sorted(h1), sorted(h2), sorted(h3)]
#     heights = [sum(h) for h in stacks]
#     target = min(heights)
#     t_idex = heights.index(target)
#     reached = False   
     
#     while not reached:
#         for h in stacks[:t_idex]+stacks[t_idex+1:]:
#             diff = [i for i in h if i <= sum(h)-target]

#             for i in range(1, len(diff)):
#                 for comb in combinations(diff, i):
                    
#                     if sum(comb) == sum(h)-target:                     
#                         reached = True
#                         break
#                 if reached: break
        
#         if not reached: 
#             stacks[t_idex].pop(0)
#             target = sum(stacks[t_idex])
#     return target
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
