"""
Pow(x, n) - Medium

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

"""
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
"""

"""
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
"""

"""
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104

# -----------------
# SOLUTIONS
# -----------------

# Recursive
def my_pow(x: float, n: int) -> float:
    """
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    # Base Case (n == 0): If the exponent n is zero
    if n == 0: # O(1)
        # the function returns 1, as any number raised to the power of 0 is 1
        return 1 # O(1)
    # Negative Exponent (n < 0): If the exponent is negative
    elif n < 0: # O(1)
        # it uses the property that x^-n = 1/x^n to calculate the result
        # recursively with a positive exponent
        return 1 / (x * my_pow(x, -n - 1)) # O(1)
    # Even Exponent (n % 2 == 0): If the exponent is even
    elif n % 2 == 0: # O(1)
        # it uses the property that x^n = (x^(n/2))^2 to calculate the result
        # more efficiently by dividing the exponent by 2
        a = my_pow(x, n // 2) # O(1)
        #  and squaring the result
        return a * a # O(1)
    # General Case (n is odd): If the exponent is odd, it 
    # recursively calculates x^(n-1) and multiplies it by x
    return x * my_pow(x, n - 1) # O(1)

# -------------------
# Test Cases for my_pow(), recursive
print("Recursive:")
print(my_pow(2.00000, 10))
print(my_pow(2.10000, 3))
print(my_pow(2.00000, -2))

# -----------------
# Iterative
def my_pow2(x: float, n: int) -> float:
    """
    Time complexity: O(n)
    Space complexity: O(1) ->Constant

    The approach optimizes the calculation of powers by using the binary representation of the exponent n. 
    It squares x when b is even and multiplies a by x when b is odd.
    """
    b = n # O(1)

    # If x is 0, the 3 cases below are special cases
    if x == 0: # O(1)
        # the function returns 0 because any non-zero number raised to the power
        # of 0 is 1, but 0 raised to any power is 0
        return 0 # O(1)
    # If n is 0
    elif b == 0: # O(1)
        #  the function returns 1 because any number raised to the power of 0 is 1
        return 1 # O(1)
    # If n is negative
    elif b < 0: # O(1)
        # the function adjusts x and n accordingly, treating the problem as if it
        # were a positive exponent
        b = -b # O(1)
        x = 1 / x # O(1)

    # initializes a variable a to 1 to accumulate the result
    a = 1 # O(1)
    # a while loop that continues until the exponent b becomes 0
    while b > 0: # O(n)
        # If b is even
        if b % 2 == 0: # O(1)
            # it updates x to x * x
            x = x * x # O(1)
            # and divides b by 2
            b = b // 2 # O(1)
        # if b is odd
        else:
            # it subtracts 1 from b
            b = b - 1 # O(1)
            # and multiplies a by the current value of x
            a = a * x # O(1)
    # At the end of iteration return a
    return a # O(1)

# -------------------
# Test Cases for my_pow2(), iterative
print("------------")
print("Iterative:")
print(my_pow2(2.00000, 10))
print(my_pow2(2.10000, 3))
print(my_pow2(1.00000, -2))
