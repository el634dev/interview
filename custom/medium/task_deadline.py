"""
You are given a list of integers, where each integer represents the time taken to complete a task. 
You are also given a deadline within which all tasks must be completed.

Write a function that determines the minimum number of tasks that can be completed within the given deadline. 
You can only work on one task at a time, and each task must be completed in order (you cannot skip tasks).

For example, given the input: tasks = [4, 2, 5, 3, 1] deadline = 10

The function should return 3, as the tasks with durations 4, 2, and 3 can be completed within 
the deadline of 10 units of time.
"""

# Constraints:

# The list of tasks will have a maximum length of 1000
# The deadline will be a positive integer
# Your solution should have a time complexity of O(n log n), where n is the number of tasks.)