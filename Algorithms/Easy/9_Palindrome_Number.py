'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Example 1:
Input: 121
Output: true
Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''
'''
# Brute Force - will fail in case of integer overflow when reversed
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_x = x
        if x < 0:
            return False
        else:
            rev = 0
            while x > 0:
                temp = x % 10
                rev = rev * 10 + temp
                x = x//10

        if rev ==  original_x:
            return True
        else:
            return False


if __name__ == "__main__":
    x = 21
    sol = Solution()
    result = sol.isPalindrome(x)
    print(result)
'''
'''
# Solution 2: converting to string 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (str(x)==str(x)[::-1])


if __name__ == "__main__":
    x = 121
    sol = Solution()
    result = sol.isPalindrome(x)
    print(result)
'''

# Solution 3: reversing only half the number
# Runtime: 72 ms, faster than 61.84% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        while (x > rev):
            rev = (rev * 10) + (x % 10)
            x = x // 10

        # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == rev or x == rev//10


if __name__ == "__main__":
    x = 121
    sol = Solution()
    result = sol.isPalindrome(x)
    print(result)