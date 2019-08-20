'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''

# Solution 1: 
# Runtime: 56 ms, faster than 59.30% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.9 MB, less than 5.38% of Python3 online submissions for Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        num = roman_dict[s[len(s)-1]]
        for i in range(len(s)-2, -1, -1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                num -= roman_dict[s[i]]
            else:
                num += roman_dict[s[i]]
        return num


if __name__ == "__main__":
    s = "IX"
    sol = Solution()
    result = sol.romanToInt(s)
    print(result)