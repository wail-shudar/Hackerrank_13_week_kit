# Completed by: Wa'il Shudar

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ranks = sorted(set(ranked), reverse=True)
    i, ans = len(ranks)-1, []
    
    for score in player: 
        while (i >= 0 and score >= ranks[i]): i -= 1
        ans.append(i+2)               
    return ans

# old, slower solution
# def climbingLeaderboard(ranked, player):
#     res, ranks = [], sorted(set(ranked), reverse=True)

#     for new_score in player:        
#         for rank, score in enumerate(ranks, 1):
#             if new_score < min(ranks):
#                 res.append(len(ranks)+1)
#                 break
#             if new_score < score: pass
#             else: 
#                 res.append(rank)
#                 break
#     return res 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
