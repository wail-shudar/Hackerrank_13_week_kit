# 1. Anagram
Two words are anagrams of one another if their letters can be rearranged to form the other word. Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

**Example**

s = abccde\
Break s into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary. 

**Function Description** 

Complete the anagram function in the editor below. anagram has the following parameter(s): 
• strings: a string Returns • int:the minimum number of characters to change or -1. 
Input Format The first line will contain an integer, q, the number of test cases. Each test case will contain a string s. 

**Constraints**

* 1 < q < 100 
* 1 < Isl < 104 
* consists only of characters in the range ascii[a-z].

**Sample Input**  

    6
    aaabbb
    ab
    abc
    mnop
    xyyx
    xaxbbbxx

**Sample Output**

    3
    1     
    -1
    2
    0
    1 


**Explanation**

*Test Case #01*: We split s into two strings 81=taaa' and S2='bbb'. We have to replace all three characters from the first string with 'b' to make the strings anagrams. 

*Test Case #02*: You have to replace 'a' with 'b', which will generate "bb". 

*Test Case #03*: It is not possible for two strings of unequal length to be anagrams of one another. 

*Test Case #04*: We have to replace both the characters of first string ("mn") to make it an anagram of the other one. 

*Test Case #05*: 81 and S2 are already anagrams of one another. 

*Test Case #06*: Here 51 = "xaxb"and 52 = "bbxx". You must replace 'a' from 51 with 'b' so that 51 = "xbxb". 
