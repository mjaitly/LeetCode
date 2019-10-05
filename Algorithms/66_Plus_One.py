'''
Given a non-empty array of digits representing a non-negative integer, plus one 
to the integer.
The digits are stored such that the most significant digit is at the head of 
the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 
0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''

# Solution 1
# Runtime: 44 ms, faster than 17.65% of Python3 online submissions for Plus One.
# Memory Usage: 13.6 MB, less than 5.13% of Python3 online submissions for Plus One.

# class Solution:
#     def plusOne(self, digits):
#         carry = 0
#         for i in range(len(digits)-1, -1, -1):
#             if digits[i] + 1 > 9:
#                 if i == len(digits) - 1:
#                     digits[i] += 1 + carry
#                 else:
#                     digits[i] += carry
#                 digits[i] %= 10
#                 carry = 1
#             else:
#                 digits[i] += 1
#                 return digits

#         if carry == 1: 
#             newDigits = [0] * (len(digits) + 1)
#             newDigits[0] = 1
#             return newDigits

# Solution 2
# Runtime: 32 ms, faster than 96.89% of Python3 online submissions for Plus One.
# Memory Usage: 13.8 MB, less than 5.13% of Python3 online submissions for Plus One.

class Solution:
    def plusOne(self, digits):
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            found = False
            for i in range(len(digits)-1,-1,-1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    found = True
                    break
            if not found:
                digits = [1] + digits
        
        return digits


if __name__ == "__main__":
    sol = Solution()
    digits = [9, 9, 9, 9]
    result = sol.plusOne(digits)
    print(result)
        