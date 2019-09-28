'''
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
'''
'''
# Solution 1 - Two Pointers problem
# Runtime: 52 ms, faster than 61.12% of Python online submissions for Search a 2D Matrix II.
# Memory Usage: 15.7 MB, less than 65.00% of Python online submissions for Search a 2D Matrix II.
class Solution(object):
    def searchMatrix(self, matrix, target):
        i = len(matrix)-1
        j = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            if target < matrix[i][j]:
                i -= 1
            else:
                j += 1
        return False
'''

# Solution 2
# Runtime: 28 ms, faster than 99.66% of Python online submissions for Search a 2D Matrix II.
# Memory Usage: 14.1 MB, less than 100.00% of Python online submissions for Search a 2D Matrix II.
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        ll = 0
        rr = len(matrix[0]) - 1
        while ll <= rr and matrix:
            temp = matrix.pop(0)
            l, r = ll, rr
            while l <= r:
                mid = (l + r) // 2
                if temp[mid] == target:
                    return True
                elif temp[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                    rr = mid - 1
        return False

if __name__ == "__main__":
    matrix = [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ]
    target = 5
    sol = Solution()
    result = sol.searchMatrix(matrix, target)
    print(result)
