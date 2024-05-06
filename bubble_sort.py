"""
Implement Bubble Sort
"""

# Iterative
def bubble_sort(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    for i in range(len(nums)): # O(n)
        for j in range(len(nums) - 1): # O(n)
            if nums[i] > nums[j + 1]: # O(1)
                nums[j], nums[j + 1] = nums[j + 1], nums[j] # O(1)
    return nums # O(1) -> single action

# -------------
# Combine
# O(n * n + 3)
# n * n then reduce
# O(n * n) -> no dominant terms
# O(n^2)

# -------------
# Test Cases
print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1]))
print(bubble_sort([1, 5, 9, 10, 6, 3, 7, 4, 2]))
print(bubble_sort([]))
