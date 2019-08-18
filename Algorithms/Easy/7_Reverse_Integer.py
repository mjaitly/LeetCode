'''
Given a 32-bit signed integer, reverse digits of an integer.
Input: 123
Output: 321
Assume that your function returns 0 when the reversed integer overflows.
'''

'''
# Brute Force

class Solution:
    def reverse(self, x: int) -> int:
        new_x = 0
        while x > 0:
            temp = x%10
            new_x = new_x * 10 + temp
            x //= 10

        return new_x

if __name__ == "__main__":
    x = -123
    sol = Solution()
    result = sol.reverse(x)
    print(result)

''' 

'''
# Solution 2
# Runtime: 44 ms, faster than  of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.9 MB, less than  of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:  
        if x > 0:  # handle positive numbers  
            rev_x =  int(str(x)[::-1])  
        if x <=0:  # handle negative numbers  
            rev_x = -1 * int(str(x*-1)[::-1])  
        # handle 32 bit overflow  
        min_x = -2**31  
        max_x = 2**31 - 1  
        if rev_x not in range(min_x, max_x):  
            return 0  
        else:  
            return rev_x

if __name__ == "__main__":
    x = -123
    sol = Solution()
    result = sol.reverse(x)
    print(result)
'''

# Solution 3
# Runtime: 40 ms, faster than 58.76% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:  
        if x > 0:
            rev = int(str(x)[::-1])
        if x <= 0:
            rev = -1*int(str(x*-1)[::-1])
        if rev < -2**31 or rev > 2**31-1:
            return 0
        return rev

if __name__ == "__main__":
    x = -123
    sol = Solution()
    result = sol.reverse(x)
    print(result)

