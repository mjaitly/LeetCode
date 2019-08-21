'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
For the purpose of this problem, we will return 0 when needle is an empty string.
'''
# Runtime: 44 ms, faster than  of Python3 online submissions for Implement strStr().
# Memory Usage: 14 MB, less than of Python3 online submissions for Implement 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        l = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(haystack) >= i + l:
                    if haystack[i:i+l] == needle:
                        return i
        return -1


if __name__ == "__main__":
    haystack = "heloollollll"
    needle = "llll"
    sol = Solution()
    result = sol.strStr(haystack, needle)
    print(result)

'''
def strStr(self, haystack: str, needle: str) -> int:
    if needle in haystack: return haystack.index(needle)
    else: return -1
'''

'''
# Runtime: 36 ms, faster than  of Python3 online submissions for Implement strStr().
# Memory Usage: 14 MB, less than of Python3 online submissions for Implement 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
'''