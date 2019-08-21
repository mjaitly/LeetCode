'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

# Solution 1: 

class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = { "{": "}", "[": "]", "(": ")"}
        if len(s) % 2 != 0:
            return False
        else:
            for i in range(0, len(s)//2):
                print(i)
                if s[i] != s[i+1] and s[i] != s[len(s)-1-i]:
                    return False
        return True

if __name__ == "__main__":
    s = "()[]{}"
    sol = Solution()
    result = sol.isValid(s)
    print(result)