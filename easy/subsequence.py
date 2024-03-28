"""
Is Subsequence - Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of
the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
"""

"""
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

# --------------------
# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

# ---------------------
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one
# to see if t has its subsequence.

# In this scenario, how would you change your code?

# ---------------------
# SOLUTIONS
# ---------------------

# Two Pointers
def isSubsequence(self, s: str, t: str) -> bool:
    """
    Time Complexity: The algorithm traverses the string t once, resulting in a time complexity of O(len(t))
    Space Complexity: Constant space is used, leading to a space complexity of O(1)O(1)O(1)
    """
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

# ---------------------
# Dynamic Programming
def is_subsequence(self, s: str, t: str) -> bool:
    """
    Time Complexity: The algorithm traverses the string s once, resulting in a time complexity of O(len(s))
    Space Complexity: The algorithm creates a list of dictionaries nxt of size len(t), leading to a space complexity of O(len(t))
    """
    nxt = [{} for _ in range(len(t) + 1)]
    for i in range(len(t) - 1, -1, -1):
        nxt[i] = nxt[i + 1].copy()
        nxt[i][t[i]] = i + 1

    i = 0
    for c in s:
        if c in nxt[i]:
            i = nxt[i][c]
        else:
            return False
    return True

# ---------------------
def is_subsequence3(self, s: str, t: str) -> bool:
    """
    Time Complexity: O(len(t)) where t is the target string
    Space Complexity: O(1), constant space
    """
    # Let n and m hold the lengths of the source and target strings respectively
    n,m = len(s),len(t)
    # i and j are the two pointers initiated as 0
    i = j = 0

    # While loop until pointer has reached the end for either strings traversed
    while i < n and j < m:
        # update both pointers if match else update only target pointer j
        if s[i] == t[j]:
            i += 1
        j += 1
    # If i is the same as source string length at the end of this, we've found a substring!
    return i == n
