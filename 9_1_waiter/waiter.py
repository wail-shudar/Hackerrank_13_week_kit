#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy
#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
def isPrime(n):
    if n == 0 or n == 1: return False
    for x in range(2, n):
        if n % x == 0: return False
    else: return True
    
def waiter(number, q):
    primes = []; answers = []; number.reverse()  
    
    n = 2
    while len(primes) != q:        
        if isPrime(n): primes.append(n)
        n+=1
        
    for p in primes:        
        b = [v for v in reversed(number) if not v % p]
        a = [v for v in reversed(number) if v % p]
        
        answers+=b
        number=a
                
    return answers+number
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
