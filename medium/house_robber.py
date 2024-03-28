"""
House Robber - Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only 
constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money 
you can rob tonight without alerting the police.
"""

# ----------------
# Examples
# ----------------
"""
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""

"""
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

# ------------------
# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

def rob(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Asssign the length of nums to n
    n = len(nums)

    # Base case, where if n equals 0
    if n == 0:
        # Return 0
        return 0

    # Assign the list of [0, 0] to s0 and s1
    s0, s1 = [0, 0], [0, 0]
    # Assign s1 with the index of 0 to nums with the index of 0
    s1[0] = nums[0]

    # Loop through i while in range of 1 to n
    for i in range(1, n):
        s0[i % 2] = max(s0[(i - 1) % 2], s1[(i - 1) % 2])
        s1[i % 2] = s0[(i - 1) % 2] + nums[i]

    return max(s0[(n - 1) % 2], s1[(n - 1) % 2])

# --------------------
# Test cases for solve_house
# --------------------
print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))

# -------------------
# Dynamic Programming
def solve_dp(nums):
    """
    Time:
    Space:
    """
    a,b = 0,0

    for n in nums:
        tmp = max(a + n, b)
        a = b
        b = tmp
    return b

# --------------------
# Test cases for solve_dp
# --------------------
print("----------")
print("Dyanmic")
print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))


# -------------------
# Tabulation
def solve_tab(nums, n):
    """
    Time: O(n)
    Space: O(n)
    """
    dp = [0] * (n + 2)

    for i in range(n - 1, -1, -1):
        dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

    return dp[0]

# --------------------
# Test cases for solve_tab
# --------------------
print("----------")
print("Tabulation")
print(solve_tab([1,2,3,1], 3))
print(solve_tab([2,7,9,3,1], 2))
