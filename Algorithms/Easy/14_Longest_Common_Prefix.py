# TODO: add divide and conquer AND binary search code
'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:
All given inputs are in lowercase letters a-z.
'''
'''
# Soultion 1: using horizontal scanning
# Computational complexity: O(S) where S is the sum of length of all strings
# Space complexity: O(1) constant space requirement

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for str in strs:
            while str.startswith(prefix) == False:
                prefix = prefix[:-1]
                if prefix == "":
                    return prefix
        return prefix


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sol = Solution()
    result = sol.longestCommonPrefix(strs)
    print(result)
'''
'''
# Soultion 2: using vertical scanning
# Computational complexity: O(S) where S is the sum of length of all strings
# in the best case there are at most n*minLen comparisons where minLen is the length of the shortest string in the array.
# Space complexity: O(1) constant space requirement
# Runtime: 44 ms, faster than 39.66% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        for i in range(0, len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0: i] 

        return strs[0]

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sol = Solution()
    result = sol.longestCommonPrefix(strs)
    print(result)
'''
'''
# Solution 3: Divide and Conqure 
# Time complexity : O(S), where S is the number of all characters in the array, S=m⋅n
# Best case this algorithm performs O(minLen⋅n) 
# Space complexity : O(m⋅logn)

class Solution:
    def longestCommonPrefix(self, strs):


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sol = Solution()
    result = sol.longestCommonPrefix(strs)
    print(result)
'''

'''
# Solution 4: Binary Search 
# Time complexity : O(S⋅logn), where S is the sum of all characters in all strings.
# Best case this algorithm performs O(minLen⋅n) 
# Space complexity : O(1). We only used constant extra space.

class Solution:
    def longestCommonPrefix(self, strs):


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sol = Solution()
    result = sol.longestCommonPrefix(strs)
    print(result)
'''