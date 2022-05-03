import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Completed by: Wail Shudar
    if s==s[::-1]: return -1
    else:
        half = (len(s)-1)//2
        k = 0 if len(s)%2 else 1 
        for i in range(len(s)):
            s2= s[:i]+s[i+1:]
            if s2[:half] == (s2[half+k:])[::-1]: 
                    return i
    # alternative *faster* solution: https://www.thepoorcoder.com/author/thepoorcoder/
    # for i,j in enumerate(range(len(s)//2), 1):
    #     if s[-i] == s[j]: continue # if periferal characters match continue inward
    #     if s[j:-i]==s[j:-i][::-1]: return len(s)-i # otherwise, check if palindrome with right char removed
    #     elif s[j+1:-i+1]==s[j+1:-i+1][::-1]: return j # check with left char removed
    # return -1 # if all characters matched (palindrome) return -1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)
    #     fptr.write(str(result) + '\n')

    # fptr.close()
