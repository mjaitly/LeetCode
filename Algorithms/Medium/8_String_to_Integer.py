'''
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the
 first non-whitespace character is found. Then, starting from this character, 
 takes an optional initial plus or minus sign followed by as many numerical 
 digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral 
number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid 
integral number, or if no such sequence exists because either str is empty or 
it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
'''
# Solution 1
# Runtime: 36 ms, faster than 92.73% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 13.7 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).
'''
import re
class Solution:
    def myAtoi(self, str):
        m = re.search(r"^(([+-]\d+)|\d+)", str.strip())
        if m:
            ans = int(m.group(1))
        else:
            ans = 0
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 - 1
        else:
            return ans
'''

# Solution 2
# Runtime: 40 ms, faster than 76.08% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 13.9 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).
class Solution:
    def myAtoi(self, str):
        str = str.lstrip()
        sign = -1
        num = ""
        max = pow(2, 31) - 1  
        min = -pow(2, 31)

        for s in str:
            if (sign != 1 and sign != 0) and s == "-" and not num:
                sign = 0
            elif (sign != 1 and sign != 0) and s == "+" and not num:
                sign = 1
            elif s.isdigit():
                num += s
            else:
                break
        
        if sign == 0 and num:
            if int("-" + num) < min:
                return min
            else:
                return int("-" + num)
            
        if (sign == 1 or sign == -1) and num:
            if int(num) > max:
                return max
            else:
                return int(num)

        if not num:
            return 0

if __name__ == "__main__":
    sol = Solution()
    # str = "   -42"
    # str = "42"
    # str = "4193 with words"
    # str = "words and 987"
    # str = "-91283472332"
    # str = "         "
    # str = "+-2"
    # str = "0-1"
    str = " ++1"
    result = sol.myAtoi(str)
    print(result)