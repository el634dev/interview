"""
Rotate Array - Medium

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

"""
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

"""
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

# ------------------
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

# ------------------
# Follow up:
# Try to come up with as many solutions as you can. 
# There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# -----------------
# SOLUTIONS
# -----------------

from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Time complexity is O(n), as each element is accessed a constant number of times during the reversal process
    Space complexity is O(1), as the rotation is done in-place without using any additional storage proportional to the input size
    Do not return anything, modify nums in-place instead.
    """
    # Helper function to rotate
    def rev(l, r):
        """
        Params: l - left, r - right
        """
        # While left is less than right
        while l < r:
            # Initilize nums left and right with the value of nums right and left
            # to swap
            nums[l], nums[r] = nums[r], nums[l]
            # Increment left by 1
            l += 1
            # Increment right by 1
            r -= 1
 
    # Initilize n with the value of the length of nums
    n = len(nums)
    # Handle cases where k > n
    k %= n

    # Reverse the entire array
    rev(0, n-1)
    # Reverse the first k elements
    rev(0, k-1)
    # Reverse the remaining elements
    rev(k, n-1)

# -------------------
# Test Cases for rotate
print("Rotate:")
print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([-1,-100,3,99], 2))

# -----------------------
# Two pointers
def rotate_2(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def twopt(arr, i, j):
        while (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr

    if k > len(nums):
        k %= len(nums)

    if (k > 0):
        twopt(nums, 0, len(nums) - 1)  # rotate entire array
        twopt(nums, 0, k - 1)          # rotate array upto k elements
        twopt(nums, k, len(nums) - 1)  # rotate array from k to end of array

# -------------------
# Test Cases for rotate_2, two pointers
print("Two pointers:")
print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([-1,-100,3,99], 2))

# -----------------------
# One liner
def rotate_3(nums: List[int], k: int) -> None:
    """
    Time complexity: O(a to the power of -1 (n))
    Space complexity: O(log log (n))
    Do not return anything, modify nums in-place instead.
    """
    nums[:] = (nums[:-k%len(nums)][::-1] + nums[-k%len(nums):][::-1])[::-1]

# -------------------
# Test Cases for rotate_2, one liner
print("One Liner:")
print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([-1,-100,3,99], 2))
