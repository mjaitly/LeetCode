'''
Given a string, find the length of the longest substring without repeating 
characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a 
substring.

aabcc, dvdf, aab, abcdvdf, abcad
'''
# Solution 1
# Runtime: 72 ms, faster than 57.94% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def lengthOfLongestSubstring(self, s):
        letterDict = {}
        start, maxLength = 0, 0
        for idx, letter in enumerate(s):
            if letter in letterDict:
                start = max(start, letterDict[letter]+1)
                print("start ", start)
            letterDict[letter] = idx
            maxLength = max(maxLength, idx - start+1)
            print("maxLength ", maxLength)
        return maxLength

if __name__ == "__main__":
    # s = "aabcc"
    s = "pwwkew"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print(result)
