from typing import List

"""
3Sum - Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

"""
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

"""
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
"""

"""
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
""" 

# ----------------
# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


# ----------------
# SOLUTIONS
# ----------------

# Brute Force Approach
def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    numbers = set()
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
        for j in range(i + 1,n - 1):
            for k in range(j + 1, n):
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    numbers.add((nums[i], nums[j], nums[k]))
    return numbers

print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([0,1,1]))
print(three_sum([0,0,0]))
print("------------------")

# ----------------------------
# Optimised Approach
def three_sum_2(nums: List[int]) -> List[List[int]]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Store numbers in a set, no duplicates allowed
    numbers = set()
    # Sort the nums in ascending order
    nums.sort()
    # Store the length of nums
    n = len(nums)

    for i in range(n - 2):
        j = i + 1
        k = n - 1
        # While j is less than k
        while j < k:
            temp = nums[i] + nums[j] + nums[k]
            if temp == 0:
                numbers.add((nums[i], nums[j], nums[k]))
                j += 1
            elif temp > 0:
                k -= 1
            else:
                j += 1

    return numbers

print(three_sum_2([-1,0,1,2,-1,-4]))
print(three_sum_2([0,1,1]))
print(three_sum_2([0,0,0]))

# ----------------------------
# More of a production-style?
def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Time Compexlity:
    Space Compexlity:
    """
    res = set()

    #1. Split nums into three lists: negative numbers, positive numbers, and zeros
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)

    #2. Create a separate set for negatives and positives for O(1) look-up times
    n, p = set(n), set(p)

    #3. If there is at least 1 zero in the list, add all cases where -num exists in N and
    # num exists in P
    #   i.e. (-3, 0, 3) = 0
    if z:
        for num in p:
            if -1 * num in n:
                res.add((-1 * num, 0, num))

    #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
    if len(z) >= 3:
        res.add((0,0,0))

    #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
    #   exists in the positive number set
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            target = -1*(n[i]+n[j])
            if target in p:
                res.add(tuple(sorted([n[i],n[j],target])))

    #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
    #   exists in the negative number set
    for i in range(len(p)):
        for j in range(i + 1,len(p)):
            target = -1 * (p[i] + p[j])
            if target in n:
                res.add(tuple(sorted([p[i],p[j],target])))

    return res
