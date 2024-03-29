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
            print("ll: " + str(ll) + " rr: " + str(rr))
            temp = matrix.pop(0)
            l, r = ll, rr
            while l <= r:
                print("l: " + str(l) + " r: " + str(r))
                mid = (l + r) // 2
                print("mid: ", mid)
                if temp[mid] == target:
                    print("result: ", (rr-1, mid))
                    return True
                elif temp[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                    rr = mid - 1
        return False



# For index as return

# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix:
#             return (-1, -1)
#         row, col, size = len(matrix) - 1, 0, len(matrix[0])
#         # print("len(matrix): ", len(matrix))
#         # print("len(matrix[0]): ", len(matrix[0]))
#         while(row >= 0 and col < size):
#             ele = matrix[row][col]
#             if ele == target:
#                 return (row, col)
#             elif ele > target:
#                 row -= 1
#             else:
#                 col += 1
#         return (-1, -1)


if __name__ == "__main__":
    matrix = [
                [1,   4,  7, 11, 15, 16],
                [2,   5,  8, 12, 19, 20],
                [3,   6,  9, 16, 22, 23],
                [10, 13, 14, 17, 24, 25],
                [18, 21, 23, 26, 30, 31]
            ]
    target = 20
    sol = Solution()
    result = sol.searchMatrix(matrix, target)
    print(result)

