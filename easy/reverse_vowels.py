"""
Reverse Vowels of a String - Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, 
more than once.
"""

# -------------
# Example 1:

# Input: s = "hello"
# Output: "holle"

# -------------
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 
# --------------
# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

# -------------
# SOLUTIONS
# -------------

def reverse_vowels(s: str) -> str:
    """
    Time Complexity: O(n), iterates through the string once and n is the length 
    of the input string
    Space Complexity:  O(n), uses additional space to store the list of characters and
    n is the length of the input string
    """
    # initialize i to 0
    i = 0 # O(1)
    # initialize j to the end of the string
    j = len(s) - 1 # O(1)
    # Covert the input string into a list of characters
    s = list(s) # O(1)

    # Iterate through the string while i is less than j
    while i < j: # O(n)
        # If i and j is in our list of characters and a vowel(lower or upper)
        if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU": # O(1)
            # Swap both pointers
            s[i], s[j] = s[j], s[i] # O(1)
            # Increment i by 1
            i = i + 1 # O(1)
            # Decrement j by 1
            j = j - 1 # O(1)
        # If i is a vowel
        elif s[i] in "aeiouAEIOU": # O(1)
            # Decrement j by 1
            j = j - 1 # O(1)
        # If not then
        else: # O(1)
            # Increment i by 1
            i = i + 1 # O(1)

    # Join or concatenate the list of characters at the end of the loop
    # with a space
    return "".join(s) # O(1)

# ---------------------------
# Two Pointers
def reverse_vowels2(s: str) -> str:
    """
    Time Complexity: O(n), iterates through the string once and n is the length 
    of the input string
    Space Complexity:  O(n), uses additional space to store the list of characters and
    n is the length of the input string
    """
    # initialize one pointer to the start of the string
    start = 0 # O(1)
    # initialize one pointer to the end of the string
    end = len(s) - 1 # O(1)
    # List of vowel characters, both lower and uppercase
    vowels = ['a', 'e', 'i', 'o', 'u'] # O(1)

    # Covert the input string into a list of characters for easy swapping
    s = list(s) # O(1)
    # Iterate through the string using both pointers
    while (start < end): # O(n)
        # If the character at position start is not a vowel
        if s[start].lower() not in vowels: # O(1)
            # Increment start by 1
            start += 1 # O(1)
        # If the character at position end is not a vowel
        elif s[end].lower() not in vowels: # O(1)
            # Decrement end by 1
            end -= 1 # O(1)
        # If both characters are at the start and end
        else:
            # Swap both pointers
            s[start], s[end] = s[end], s[start] # O(1)
            # then increment by 1
            start += 1 # O(1)
            # and decrement by 1
            end -= 1 # O(1)
    # Join or concatenate the list of characters at the end of the loop
    # with a space
    return "".join(s) # O(1)
