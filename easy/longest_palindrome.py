"""
Longest Palindrome - Easy

Given a string s which consists of lowercase or uppercase letters, return the length 
of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

# ------------------
# Constraints:
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

# ------------------
# SOLUTIONS
import collections
from typing import Counter


# Bitwise
"""
Use a bitfield to record whether a character is available for pairing.

For each character in the string, calculate a bit position where it should 
appear in the bitfield. If that bit is not set, then set it. If it's 
already set, then that character is available for pairing. Increase the 
result by 2 and clear the bit.

After pairing up as many characters as possible, if there are any 
characters left in the bitfield, increase result by 1.

52 bits are needed for the bitfield, but for simplicity we'll use 
58 bits (ord('z') - ord('A') + 1)
"""
def longest_palindrome(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    bits = 0

    result = 0
    for ch in s:
        bit = 1 << (ord(ch) - 65)
        if bits & bit:
            bits ^= bit
            result += 2
        else:
            bits |= bit

    if bits:
        result += 1

    return result

print(longest_palindrome("abccccdd"))
print(longest_palindrome("a"))

# ------------------
# Use a Set
def longest_palindrome_2(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    k,p = 1,0
    if len(set(s)) == 1:
        return len(s)

    c = Counter(s)
    for i in c:
        if c[i] % 2 == 0:
            p += c[i]

        if c[i] % 2 != 0:
            if k == 1:
                p += c[i]
                k = 0
            else:
                p += (c[i] - 1)
    return p

print(longest_palindrome_2("abccccdd"))
print(longest_palindrome_2("a"))

# ------------------
# Hash Table
def longest_palindrome_3(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count = {} # Hash Table
    ans = []   # every word's frequency
    odd = 0     # store an odd number's frequency

    for word in s:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    for times in count.values():
        ans.append(times)
        if times % 2 != 0:
            # calculate an odd number's frequency
            odd += 1
    if odd != 0:
        return sum(ans) - odd + 1
    elif odd == 0:
        return sum(ans) - odd

print(longest_palindrome_3("abccccdd"))
print(longest_palindrome_3("a"))
