''''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
# Solution 1: stack implementation
# Runtime: 32 ms, faster than 94.12% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

if __name__ == "__main__":
    s = "}{"
    sol = Solution()
    result = sol.isValid(s)
    print(result)      
        