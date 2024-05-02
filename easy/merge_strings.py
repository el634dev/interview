"""
Merge String Alternatively - Easy

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with 
word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

"""
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

"""
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
"""

"""
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""

# -----------------
# Constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


# -----------------
# SOLUTIONS
# -----------------

# O(n)
def merge_alternately(word1: str, word2: str) -> str:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    res = "" # O(1)
    for i in range(min(len(word1),len(word2))): # O(n)
        res += word1[i]  # O(1)
        res += word2[i]  # O(1)

    if len(word1) > len(word2):  # O(1)
        res += word1[i+1:]  # O(1)
    else:  # O(1)
        res += word2[i+1:]  # O(1)
    return res  # O(1)

print(merge_alternately("abc", "pqr"))
print(merge_alternately("ab", "pqrs"))
print(merge_alternately("abcd", "pq"))

# -----------------
# Two Pointers
def merge_alternately_pointer(word1: str, word2: str) -> str:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        i, j = 0, 0  # O(1)
        ans = []  # O(1)

        while i < len(word1) and j < len(word2):  # O(n)
            ans.append(word1[i])  # O(1)
            ans.append(word2[j])  # O(1)
            i += 1  # O(1)
            j += 1  # O(1)
        while i < len(word1): # O(n)
            ans.append(word1[i])  # O(1)
            i += 1  # O(1)
        while j < len(word2): # O(n)
            ans.append(word2[j]) # O(1)
            j += 1  # O(1)
        return "".join(ans) # O(1)

# --------------------
# Test cases, two pointers
print(merge_alternately_pointer("abc", "pqr"))
print(merge_alternately_pointer("ab", "pqrs"))
print(merge_alternately_pointer("abcd", "pq"))

# --------------------
# Using Zip, 2 lines
from itertools import zip_longest

def merge_alternately_zip(word1: str, word2: str) -> str:
    """
    Time Complexity: O(1) -> Constant
    Space Complexity: O(1) -> Constant
    """
    return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue = "")) # O(1)

# --------------------
# Using Zip, 1 lines
def merge_alternately_zip_2(word1: str, word2: str) -> str:
    """
    Time Complexity:  O(1) -> Constant
    Space Complexity: O(1) -> Constant
    """
    return "".join(a + b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):] # O(1)
