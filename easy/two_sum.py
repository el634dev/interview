"""
Two Sum - Easy

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

You can return the answer in any order.
"""

# ----------------
"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# ----------------
"""
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

# ----------------
"""
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

# ---------------
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
# ----------------

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# -----------------
# SOLUTIONS
# -----------------
from typing import List

# Efficient Hash Map Solution: Utilizing a hash map for constant-time lookups,
# this method is efficient and commonly used
def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Runtime Comp: O(n), where n is the number of elements in the input list nums.
    This is because the function uses a single loop to iterate through the elements of the input list 
    and store the indices of the elements in a dictionary
    """
    # Store the indices of the numbers
    num_indices = {}

    # Iterate through the list of numbers to find the pair that meets
    # the condition
    for i, num in enumerate(nums):
        # Calculate the value needed to achieve the target sum
        # by subtracting target from num
        target_val = target - num

        # Check if target_val is present in our dictionary
        if target_val in num_indices:
            # Return the indices of those numbers
            return [num_indices[target_val ], i]
        # If not found then add the current number and its index to the dictionary
        # for future reference
        num_indices[num] = i

# -------------------
# Test Cases for two_sum()
print(two_sum([2,7,11,15], target = 9))
print(two_sum([3,2,4], target = 6))
print(two_sum([3,3], target = 6))

# -----------------------------
# Brute Force Solution: This is often considered the simplest but less efficient approach,
# as it involves checking every pair of elements
def two_sum2(nums: List[int], target: int) -> List[int]:
    """
    Runtime Comp: O(n^2), where n is the number of elements in the input list nums. 
    This is because it has two nested loops that iterate over all pairs of indices in the list, 
    resulting in a quadratic time complexity
    """
    # Get length of nums(list)
    n = len(nums)
    
    # Iterate over all pairs of indices i and j in the list
    # such that j is greater than i
    for i in range(n):
        # For each pair of indices
        for j in range(i + 1, n):
            # Check the sum of the elements at those indices is equal to the target
            if nums[i] + nums[j] == target:
                # Return if found
                return [i, j]
    # Else return a empty list
    return []

# -------------------
# Test Cases for two_sum()
print("Brute Force")
print(two_sum2([2,7,13,11], target = 9))
print(two_sum2([3,2,4], target = 6))
print(two_sum2([3,2], target = 5))

# -------------------
# Clarfying Questions
# -------------------
