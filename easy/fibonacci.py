"""
Fibonacci Number - Easy

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""

# ----------------
"""
Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
"""

# ----------------
"""
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
"""

# ----------------
"""
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

# ---------------
# Constraints:
# 0 <= n <= 30
# ---------------

# ---------------
# Fib Sequence Recursive Tree
# ----------------

#                          fib(5)
#                     /                \
#               fib(4)                 fib(3)
#             /        \              /       \ 
#         fib(3)      fib(2)         fib(2)   fib(1)
#        /    \       /    \        /      \
#  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
#  /     \
# fib(1) fib(0)

# -----------------
# SOLUTIONS
# -----------------

# Recursive Solution
def fib(n: int) -> int:
    """
    Time Comp: O(1)
    Space Comp: O(1)
    """
    # Base case when n is 0 or 1
    if n <= 1: # O(1)
        return n # O(1)
    # Recursively calculate the Fib numbers and return the sum
    return fib(n - 1) + fib(n - 2) # O(1)

# -------------------
# Test Cases for fib()
print("Recursive:")
print(fib(1))
print(fib(3))
print(fib(5))

# -------------------
# Iterative Solution
# Precomputes the next element in the Fib Sequence in advance
# to perform 'caching' trick iteratively
def fib2(n: int) -> int:
    """
    Time Complexity: 0(n)
    """
    # Check if n equals 0 or 1, can omit
    if n == 0 or n == 1: # O(1)
        return n # O(1)

    las, nxt = 0, 1 # O(1)
    for _ in range(n): # O(n)
        las, nxt = nxt, las + nxt # O(1)
    return las # O(1)

# -------------------
# Test Cases for fib2()
print("Iterative:")
print(fib(0))
print(fib(5))
print(fib(4))

# -------------------
# Clarfying Questions
# -------------------

# Can I assume the data type will always be numeric?
