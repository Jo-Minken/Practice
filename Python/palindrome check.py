"""
Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, 
e.g., madam,kayak,racecar, or a phrase "nurses run". 

Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. 
Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.

"""

import math

def palindrome(s):
    length = len(s)
    half = math.floor(length/2)
    
    for i in range(half):
        if not s[i] == s[length-i-1]:
            return False
    
    return True

#     return s == s[::-1]

palindrome('helleh')