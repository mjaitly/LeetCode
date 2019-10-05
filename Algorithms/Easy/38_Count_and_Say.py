'''
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     312211
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
'''

# Soultion 1
# Runtime: 32 ms, faster than 98.70% of Python3 online submissions for Count and Say.
# Memory Usage: 14.5 MB, less than 6.38% of Python3 online submissions for Count and Say.
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        s = "11"
        i = 3
        while i < n+1:
            s += "$"
            new_s = ""
            count = 1
            for j in range(1, len(s)):
                if s[j-1] == s[j]:
                    count += 1
                else:
                    print(count)
                    new_s += str(count) + s[j-1]
                    count = 1
            s = new_s
            i += 1
        return s

# class Solution:
#     def countAndSay(self, n):
#         for i in range(3, n + 1): 
#             s += '$'
#             l = len(s) 
#             cnt = 1
#             tmp = ""
#             # Process previous term to 
#             # find the next term 
#             for j in range(1 , l): 
                
#                 # If current character 
#                 # does't match 
#                 if (s[j] != s[j - 1]): 
                    
#                     # Append count of  
#                     # str[j-1] to temp 
#                     tmp += str(cnt + 0) 
    
#                     # Append str[j-1] 
#                     tmp += s[j - 1] 
    
#                     # Reset count 
#                     cnt = 1
#                 else: 
#                     cnt += 1
    
#             # Update str 
#             s = tmp 
#         return s
  
if __name__ == "__main__":
    n = 6
    sol = Solution()
    result = sol.countAndSay(n)
    print(result)