import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

    
def anagram(s):
    # Completed by: Wail Shudar
    l = len(s)//2
    if not len(s)%2==0: return -1    

    a = {i:s[:l].count(i) for i in set(s[:l])}
    b = {i:s[l:].count(i) for i in set(s[l:])}

    # dict of elements only in a and their frequency
    a_not_b_freq = sum([a[k] for k in set(s[:l])-set(s[l:])])
    # dict of the elements in a that must be changed that are common to b
    a_cross_freq = sum([a[k]-b[k] for k in set(s[l:])&set(s[:l]) if a[k]>b[k]])
    
    return a_not_b_freq + a_cross_freq
        

if __name__ == '__main__':
    print(os.environ['OUTPUT_PATH'])
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
