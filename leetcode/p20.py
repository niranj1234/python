# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        a= []
        mapp = {")":"(","}":"{", "]":"[" }

        for i in s:
            if i in mapp.values():
                a.append(i)
            elif i in mapp.keys():
                if not a or mapp[i] != a.pop():
                    return False

        return not a
# Example usage:
s = "()[]{}"
solution = Solution()
result = solution.isValid(s)
print(result)  # Output: True 