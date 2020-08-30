"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

"""

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    for d in alphabet:
        if not d in str1:
            return False
    return True

#     str1 = str1.replace(" ", "").lower()
#     return set(str1) == set(alphabet)

ispangram("The quick brown fox jumps over the lazy dog")
