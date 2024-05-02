"""
Binary Search - Easy

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(logn) runtime complexity.

Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. 
The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N
"""

# ----------------
"""
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""

# -----------------
"""
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

# ---------------
# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

# -----------------
# SOLUTIONS
# -----------------
from typing import List

# O(logn) Solution
def search(nums: List[int], target: int) -> int:
    """
    Runtime Comp: O(logn)
    """
    # Assign left the value of 0
    left = 0 # O(1)
    # Assign right the last element by subtracting 1 from the length of nums
    right = len(nums) - 1 # O(1)

    while(left <= right): # O(n)
        middle = (left + right ) // 2 # O(1)

        if nums[middle] == target: # O(1)
            return middle # O(1)
        elif nums[middle] < target: # O(1)
            left = middle + 1 # O(1)
        else: # O(1)
            right = middle - 1 # O(1)
    return -1 # O(1)

# -------------------
# Test Cases for search()
# -------------------
print("Search 1, O(nlogn)")
print(search([-1,0,3,5,9,10], target = 9))
print(search([-2,0,3,5,9,12], target = 2))

# ---------------------
# Brute Force Solution
def search2(nums: List[int], target: int) -> int:
    """
    Time Complexity: O(n)
    """
    # iterates over the elements of the nums array
    for i in range(0 , len(nums)): # O(n)
        # checks if the current element of the array (nums[i]) is equal to the target value
        if target == nums[i]: # O(1)
            # returns the current index i, which is the position of the target in the array
            return i # O(1)
    # If target value is not present in the nums array, return -1
    return -1 # O(1)

# -------------------
# Test Cases for search2()
# -------------------
print("------------")
print("Search 2, Brute Force")
print(search2([-1,0,3,5,9,12], target = 9))
print(search2([-1,0,3,5,9,12], target = 2))

# Optimized Solution?, Optimized is considered O(logn)
def search3(nums: List[int], target: int) -> int:
    """
    Time Comp: O(n)
    Space Comp: O(1)
    """
    start , end = 0 , len(nums) - 1 # O(1)

    while start <= end : # O(n)
        mid = (start+end) // 2 # O(1)
        if nums[mid] == target: # O(1)
            return mid # O(1)
        elif target < nums[mid]: # O(1)
            end = mid -1 # O(1)
        else : # O(1)
            start = mid + 1 # O(1)
    return -1 # O(1)

# -------------------
# Test Cases for search3()
# -------------------
print("------------")
print("Search 3, Optmized?")
print(search3([-1,0,3,5,9,12], target = 9))
print(search3([-1,0,3,5,9,12], target = 2))
print(search3([], target = 0))

# ------------------------------
## EXTRA NOTES
# ------------------------------

# ------------------------------
# How to apply a Binary Search?
# ------------------------------
# To apply a Binary Search algorithm: 👈
#  1. The data structure must be sorted.
#  2. Access to any element of the data structure takes constant time.
# ------------------------------

# ------------------------------
# How to Solve Step by Step
# -------------------------
"""
Binary Search Algorithm: 👈
In this algorithm,
    1. Divide the search space into two halves by finding the middle index “mid”.
        a.To Find the mid, assign the value of low + (high - low) / 2
    2. Compare the middle element of the search space with the key.

    3. If the key is found at middle element, the process is terminated.

    4. If the key is not found at middle element, choose which half will be used as the next search space.

    5. If the key is smaller than the middle element, then the left side is used for next search.

    6. If the key is larger than the middle element, then the right side is used for next search.

    7. This process is continued until the key is found or the total search space is exhausted.
"""
