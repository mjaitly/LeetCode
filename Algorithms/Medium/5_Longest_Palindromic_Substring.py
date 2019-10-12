'''
Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''
# Solution 1 - Expand Around Center -  O(n^2) time using constant space.
# Runtime: 928 ms, faster than 82.53% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.9 MB, less than 22.69% of Python3 online submissions for Longest Palindromic Substring.
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return s

        start, end = 0, 0

        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start: end + 1]

def expandAroundCenter(s, left, right):
    while (left >= 0 and right < len(s)) and (s[left] == s[right]):
        left -= 1
        right += 1

    return right - left - 1

if __name__ == "__main__":
    sol = Solution()
    s = "ababababc"
    result = sol.longestPalindrome(s)
    print(result)

'''
public String longestPalindrome(String s) {
    if (s == null || s.length() < 1) return "";
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}

private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--;
        R++;
    }
    return R - L - 1;
}
'''