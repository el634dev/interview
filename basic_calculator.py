"""
Basic Calculator - Hard

Given a string s representing a valid expression, implement a basic calculator to 
evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as 
mathematical expressions, such as eval().
"""

"""
Example 1:

Input: s = "1 + 1"
Output: 2
"""

"""
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
"""

"""
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""

# -----------------
# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).

# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.

# -----------------
# SOLUTIONS
# -----------------

# Recursion
def calculate(s):
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def evaluate(i):
        """
        Time Complexity: O(n) where n is the string called s
        Evalute is the helper function
        """
        res, digit, sign = 0, 0, 1 # O(1)

        while i < len(s): # O(n)
            if s[i].isdigit(): # O(1)
                digit = digit * 10 + int(s[i]) # O(1)
            elif s[i] in '+-': # O(1)
                res += digit * sign # O(1)
                digit = 0 # O(1)
                sign = 1 if s[i] == '+' else -1 # O(1)
            elif s[i] == '(': # O(1)
                subres, i = evaluate(i+1) # O(1)
                res += sign * subres # O(1)
            elif s[i] == ')': # O(1)
                res += digit * sign # O(1)
                return res, i # O(1)
            i += 1 # O(1)

        return res + digit * sign # O(1)

    return evaluate(0) # O(1)

print(calculate("1 + 1"))
print(calculate(" 2-1 + 2 "))
print(calculate("(1+(4+5+2)-3)+(6+8)"))
print("-----------------")

# -----------------
# Stack
def calculate_2(s: str) -> int:
    """
    Time Complexity: O(n) where n is the string called s
    Space Complexity: O(n) where n is the string called s
    """
    output, curr, sign, stack = 0, 0, 1, [] # O(1)
    for c in s: # O(n)
        if c.isdigit(): # O(1)
            curr = (curr * 10) + int(c) # O(1)
        elif c in '+-': # O(1)
            output += curr * sign # O(1)
            curr = 0 # O(1)
            
            if c == '+': # O(1)
                sign = 1 # O(1)
            else:
                sign = -1 # O(1)
        elif c == '(': # O(1)
            stack.append(output) # O(1)
            stack.append(sign) # O(1)
            sign = 1 # O(1)
            output = 0 # O(1)
        elif c == ')': # O(1)
            output += curr * sign # O(1)
            output *= stack.pop() # sign, O(1)
            output += stack.pop() # last output, O(1)
            curr = 0 # O(1)

    return output + (curr * sign) # O(1)

print(calculate_2("1 + 1"))
print(calculate_2(" 2-1 + 2 "))
print(calculate_2("(1+(4+5+2)-3)+(6+8)"))
