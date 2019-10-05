'''
Given a string s consists of upper/lower-case alphabets and empty space 
characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space 
characters only.

Input: "Hello World"
Output: 5
'''

# Solution 1
# Runtime: 40 ms, faster than 31.86% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Length of Last Word.

# class Solution:
#     def lengthOfLastWord(self, s):
#         if not s:
#             return 0
#         else:
#             words = s.split(" ")
#             print(words)
#             for word in words[::-1]:
#                 print(word)
#                 if len(word) > 0:
#                     return len(word)
#         return 0

# Solution 2
# Runtime: 20 ms, faster than 31.86% of Python3 online submissions for Length of Last Word.
class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        print(s)
        if s == "":
            return 0
        else:
            ans = 0
            for i in s[::-1]:
                print(i)
                if i == " ":
                    return ans
                else:
                    ans+=1
            return ans

if __name__ == "__main__":
    sol = Solution()
    s = "Hello world "
    result = sol.lengthOfLastWord(s)
    print(result)

