"""
You are given a list of integers, which represents the scores of students in a class. The scores range from 0 to
100. Your task is to determine the average score of the students in the class, rounded to the nearest whole number.

Write a function averageScore(scores) that takes in a list of integers scores and returns the 
average score as an integer.
"""

# Example:
# Input: [75, 80, 90, 85, 95] Output: 85
# Input: [60, 70, 80, 90, 100] Output: 80
# Input: [80, 85, 90] Output: 85

# Example 2:
# Input: [80, 85, 90, 100, 95] Output: 95
# Input: [50, 60, 70, 80, 90] Output: 70
# Input: [90, 95, 105] Output: 90

# --------------------------
# SOLUTIONS
# --------------------------

from statistics import mean
# import numpy

def average_score(scores):
    """
    Using Python's sum function
    """
    # Create a list of scores
    list_of_scores = list(scores)
    # Sum all the numbers together
    sum_of_scores = sum(list_of_scores)

    # Divide the sum by the number in list and store it in a variable
    score_avg = sum_of_scores / len(list_of_scores)
    # Return the number that is the result of division
    return round(score_avg, 3)

# ----------------------
# Test Cases
# ----------------------
print(average_score([40, 90, 20, 80, 75]))
print(average_score([80, 90]))
print(average_score([30, 40, 20]))

# ----------------------
# Using the mean function
def average_score_2(scores):
    """
    Using Python's sum function
    """
    # Create a list of scores
    list_of_scores = list(scores)
    # Sum all the numbers together
    sum_of_scores = mean(list_of_scores)

    # Divide the sum by the number in list and store it in a variable
    score_avg = sum_of_scores / len(list_of_scores)
    # Return the number that is the result of division
    return round(score_avg, 3)

# ----------------------
# Test Cases
# ----------------------
print("Using the mean function")
print(average_score_2([40, 90, 20, 80, 75]))
print(average_score_2([80, 90]))
print(average_score_2([30, 40, 20]))


# ----------------------
# Using the mean function
def average_score_npy(scores):
    """
    Using numpy
    """
    # Create a list of scores
    list_of_scores = list(scores)
    # Sum all the numbers together using numpy.average
    sum_of_scores = mean(list_of_scores)

    # Divide the sum by the number in list and store it in a variable
    score_avg = sum_of_scores / len(list_of_scores)
    # Return the number that is the result of division
    return round(score_avg, 3)

# ----------------------
# Test Cases
# ----------------------
print("Using numpy")
print(average_score_npy([40, 90, 20, 80, 75]))
print(average_score_npy([80, 90]))
print(average_score_npy([30, 40, 20]))
