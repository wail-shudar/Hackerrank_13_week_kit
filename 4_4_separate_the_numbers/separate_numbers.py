import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):
    for i in range(1, len(s)//2+1):
        sub = s[:i]
        if isSeq(s, sub):return print("YES",sub)
    return print("NO")

def isSeq(s, sub):
    if not s: return True
    if s.startswith(sub): return isSeq(s[len(sub):], str(int(sub)+1))  
    return False
    

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
