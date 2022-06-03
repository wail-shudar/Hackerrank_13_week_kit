#!/bin/python3
# Completed by: Wa'il Shudar
import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(*args):
    
    prices, profit = args[0], args[1] if len(args)>1 else 0
    
    if prices:
        idx = prices.index(max(prices))        
        profit += max(prices)*len(prices[:idx])-sum(prices[:idx])
        return stockmax(prices[idx+1:], profit)
    else: return profit

# my original, non-recursive solution
# def stockmax(prices):
    
#     l = len(prices)
#     cost = profit = 0
    
#     while prices and prices.index(max(prices)) < l:
#         mx = max(prices)
#         mxi = prices.index(mx)
#         cost+=sum(prices[:mxi])
#         profit+= mx*len(prices[:mxi])
#         prices = prices[mxi+1:]
#     return profit-cost

# alt solution by another user
# def stockmax(prices):
#     max_price = 0
#     profit = 0
#     for p in reversed(prices):
#         max_price = max((max_price, p))
#         profit += max_price - p
#     return profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
