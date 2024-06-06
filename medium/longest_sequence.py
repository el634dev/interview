"""
Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the 
longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

# ----------------
# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its 
# length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# ----------------
# SOLUTIONS
from typing import List


class Loop:
    """Use a loop and set"""
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n), we loop through nums once
        Space Complexity: O(n), need a set to store the list
        """
        sorted_nums = set(nums)
        # Initilize a new counter to store the longest sequence
        longest_seq = 0

        for n in nums:
            # check to see if its the start of the sequence
            if (n - 1) not in sorted_nums:
                # Initilize a new counter to store the length number
                nums_len = 0
                # Keep looping while the sum of n + nums_len is in our set
                while n + nums_len in sorted_nums:
                    # Increment the length number counter
                    nums_len += 1
                # Initilize longest to be the max value of nums_len and longest sequence
                longest = max(nums_len, longest_seq)
        return longest

# ------------------
class UnionFind:
    """Union Find class"""
    def __init__(self, nums):
        self.parents = {num: num for num in nums}
        self.size = {num:1 for num in nums}
        self.max_l = 1
    
    def find_parent(self, n):
        """Find the parent"""
        if self.parents[n]!=n:
            self.parents[n] = self.find_parent(self.parents[n])
        return self.parents[n]
    
    # ---------------------
    def union(self, n1, n2):
        """Union"""
        p1, p2 = self.find_parent(n1), self.find_parent(n2)

        # Check if parent 1 is not equal to parent 2
        if p1 != p2:
            # Check if parent 1 is greater than parent 2
            if self.size[p1] > self.size[p2]:
                # Re-assign parent 2 to parent 1
                self.parents[p2] = p1
                self.size[p1] += self.size[p2]
                self.max_l = max(self.max_l, self.size[p1])
            else:
                self.parents[p1] = p2
                self.size[p2] += self.size[p1]
                self.max_l = max(self.max_l, self.size[p2])

class UnionSolution:
    """Use the Union Find Class"""
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n), use a loop to go through nums
        Space Complexity: O(n^2), using a class?
        """
        if not nums:
            return 0
        u = UnionFind(nums)

        for i in nums:
            if i+1 in u.parents:
                u.union(i, i+1)
        return u.max_l
