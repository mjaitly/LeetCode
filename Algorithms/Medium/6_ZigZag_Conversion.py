'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of 
rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

_   _   _   _
_ _ _ _ _ _ _
_   _   _

_   _   _   _
_   _ _ _ _ _
_ _  _   _
_
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        return s


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    result = sol.convert(s, numRows)
    print(result)