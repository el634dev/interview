"""
The kth Factor of n - Medium

You are given two positive integers n and k. 
A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has 
less than k factors.
"""

"""
Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
"""

"""
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
"""

"""
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
"""

# -----------------
# Constraints:
# 1 <= k <= n <= 1000

# -----------------
# Follow up:
# Could you solve this problem in less than O(n) complexity?

def kth_factor(n, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Initialize count to 0, used to keep track of the # of factors
    count = 0

    # Iterate through all integers from 1 to n inclusive
    for i in range(1,n + 1):
        # If n is divisble by i using the modulo operator
        if n % i == 0:
            # Increment count
            count += 1
            # If current count equals k
            if count == k:
                # Return the current factor
                return i
    # Return -1, indicates that there are fewer than k factors of n
    return -1

# ------------------------
def kth_factor2(n: int, k: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # If k is less than n
    if k > n:
        # Return -1
        return -1

    # Initlized i to 1
    i = 1
    # Initlized i to 0
    count = 0

    # Looping through i while i less or equal to n
    while i <= n:
        # If n is divisble by i using the mod operator and
        # the remainder is equal to 0
        if n % i == 0:
            # Increment the current count by 1
            count += 1

        # If the current count is equal to k
        if count == k:
            # Return i
            return i

        # Increment i by 1
        i += 1    
    # Return -1
    return -1
