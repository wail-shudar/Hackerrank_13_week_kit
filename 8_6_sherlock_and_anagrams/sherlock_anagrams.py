#!/bin/python3
# Completed by: Wa'il Shudar
import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isAnagram(s1, s2):
    return True if sorted(s1) == sorted(s2) else False
    
def sherlockAndAnagrams(s):
    pairs = 0    
    for i in range(1, len(s)): # loop for substring lengths
        for j in range(0, len(s)-i): # loop for traversing
            for k in range(j+1, len(s)-i+1): # loop for comparison
                if isAnagram(s[j:j+i], s[k:k+i]): pairs+=1
    return pairs

# alt. solution by: https://www.hackerrank.com/VictorSGhosh
# def sherlockAndAnagrams(s):
#     substring_count = Counter ("".join (sorted (s[j:i+j])) 
#     for i in range(1, len(s)) for j in range(len(s)-i+1))    
#     return sum([(x*(x-1))//2 for x in substring_count.values()])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
