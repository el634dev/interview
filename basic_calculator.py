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
        res, digit, sign = 0, 0, 1

        while i < len(s):
            if s[i].isdigit():
                digit = digit * 10 + int(s[i])
            elif s[i] in '+-':
                res += digit * sign
                digit = 0
                sign = 1 if s[i] == '+' else -1
            elif s[i] == '(':
                subres, i = evaluate(i+1)
                res += sign * subres
            elif s[i] == ')':
                res += digit * sign
                return res, i
            i += 1

        return res + digit * sign

    return evaluate(0)

print(calculate("1 + 1"))
print(calculate(" 2-1 + 2 "))
print(calculate("(1+(4+5+2)-3)+(6+8)"))
print("-----------------")

# -----------------
# Stack
def calculate_2(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    output, curr, sign, stack = 0, 0, 1, []
    for c in s:
        if c.isdigit():
            curr = (curr * 10) + int(c)

        elif c in '+-':
            output += curr * sign
            curr = 0
            if c == '+':
                sign = 1

            else:
                sign = -1

        elif c == '(':
            stack.append(output)
            stack.append(sign)
            sign = 1
            output = 0

        elif c == ')':
            output += curr * sign
            output *= stack.pop()    #sign
            output += stack.pop()    #last output
            curr = 0

    return output + (curr * sign)

print(calculate_2("1 + 1"))
print(calculate_2(" 2-1 + 2 "))
print(calculate_2("(1+(4+5+2)-3)+(6+8)"))
