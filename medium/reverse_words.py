"""
Reverse Words in a String - Medium

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a 
single space separating the words.
Do not include any extra spaces.
"""

"""
Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
"""

"""
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""

"""
Example 3:

Input: s = "a good example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

"""
Example 4:

Input: s = ""
Output: 
Explanation: There is no string to reverse
"""

# ---------------------------
# Constraints:
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

# ---------------------------
# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?


# ---------------------------
# SOLUTIONS
# ---------------------------

# One Liner
def reverse_words(s: str) -> str:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # 
    return " ".join(reversed(s.split()))

# ---------------------------
# Test Cases for one liner
print(reverse_words("One liner"))
print(reverse_words("the sky is blue"))
print(reverse_words("the cow jumped"))
print(reverse_words("the fox"))

# ---------------------------
# Two Pointers
def reverse_words2(s: str) -> str:
    s = s.split()

    # Two pointers approach
    left, right = 0, len(s) - 1

    while left < right:
        # Swap the words
        s[left], s[right] = s[right], s[left]
        # Move pointers
        left += 1
        right -= 1

    # Convert the list back to a string
    return ' '.join(s).strip()

# ---------------------------
# Test Cases for two pointers
print(reverse_words2("Two pointers"))
print(reverse_words2("the sky is blue"))
print(reverse_words2("the cow jumped"))
print(reverse_words2("the fox"))

# ---------------------------
# Built-Functions
def reverseWords(s: str) -> str:
    # Split the input string by spaces and filter out empty  
    # strings
    words = s.split()
    
    # Reverse the list of words
    words.reverse()
    
    # Join the reversed words into a single string with a
    # space between each word
    return ' '.join(words)

# ---------------------------
# Test Cases for bulit-in
print(reverseWords("the sky is blue"))
print(reverseWords("the cow jumped"))
print(reverseWords("the fox"))
print(reverseWords(""))
