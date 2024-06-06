"""
Contains Duplicate - Easy

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

# --------------
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# --------------
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# --------------
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# SOLUTIONS

# Brute Force (Time Limit Exceeds on LC)

# Intuition:
# The brute force approach compares each element with every other element in the array to 
# check for duplicates. 
# If any duplicates are found, it returns true. This approach is straightforward but
# has a time complexity of O(n^2), making it less efficient for large arrays.

# Explanation:
# The brute force approach involves comparing each element in the array with every other 
# element to check for duplicates. 
# If any duplicates are found, return true, otherwise return false.

from typing import List


class BruteForce:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

# -----------------------
# Sorting

# Intuition:
# The sorting approach sorts the array in ascending order and then checks for 
# adjacent elements that are the same. If any duplicates are found, it returns true. Sorting
# helps in bringing duplicates together, simplifying the check. However, sorting has a time
# complexity of O(n log n).

# Explanation:
# Another approach is to sort the array and then check for adjacent elements that are 
# the same. If any duplicates are found, return true, otherwise return false.

class Sort:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        nums.sort()
        n = len(nums)

        for i in range(1, n): # O(n)
            if nums[i] == nums[i - 1]:
                return True
        return False

# -----------------------
# Hash Set

# Intuition:
# The hash set approach uses a hash set data structure to store encountered 
# elements. It iterates through the array, checking if an element is already 
# in the set. If so, it returns true. Otherwise, it adds the element to the set.
# This approach has a time complexity of O(n) and provides an efficient way to
# check for duplicates.

# Explanation:
# A more efficient approach is to use a hash set data structure to store the 
# encountered elements. While iterating through the array, if an element is
# already present in the hash set, return true. Otherwise, add the element 
# to the hash set. If the loop completes without finding any duplicates, 
# return false.

class Set:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n), using a for loop
        Space Complexity: O(1)
        """
        contains = set()

        for num in nums: # O(n)
            if num in contains:
                return True
            contains.add(num)
        return False

# -----------------------
# Sorting

# Intuition:
# The sorting approach sorts the array in ascending order and then checks for 
# adjacent elements that are the same. If any duplicates are found, it returns true. Sorting
# helps in bringing duplicates together, simplifying the check. However, sorting has a time
# complexity of O(n log n).

# Explanation:
# Another approach is to sort the array and then check for adjacent elements that are 
# the same. If any duplicates are found, return true, otherwise return false.

class Sort:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        nums.sort()
        n = len(nums)

        for i in range(1, n): # O(n)
            if nums[i] == nums[i - 1]:
                return True
        return False

# -----------------------
# Hash Map

# Intuition:
# The hash map approach is similar to the hash set approach but also keeps 
# track of the count of occurrences for each element. It uses a hash map to 
# store the elements as keys and their counts as values. If a duplicate
# element is encountered (count greater than or equal to 1), it returns true. 
# This approach provides more information than just the presence of duplicates and
# has a time complexity of O(n).

# Explanation:
# In this approach, we iterate through the array and s
# tore each element as a key in a hash map. The value associated with each 
# key represents the count of occurrences of that element. If we encounter 
# an element that already exists in the hash map with a count greater than 
# or equal to 1, we return true, indicating that a duplicate has been found.
# Otherwise, we update the count of that element in the hash map. If we 
# complete the iteration without finding any duplicates, we return false.

class Hash:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n), using a for loop and n is the length of the array
        Space Complexity: O(1)
        """
        seen = {}

        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False
