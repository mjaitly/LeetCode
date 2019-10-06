'''
Given a positive integer n, generate a square matrix filled with elements from 
1 to n2 in spiral order.
Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
[
 [ 1, 2 ],
 [ 4, 3 ]
]
[
 [ 1,  2,  3,  4 ],
 [ 12, 13, 14, 5 ],
 [ 11, 16, 15, 6 ],
 [ 10, 9,  8,  7 ],
]
'''

'''
class Solution:
    def generateMatrix(self, n):
        matrix = [x[:] for x in [[0] * n] * n]
        startNum = 1
        for i in range(n//2):
            matrix, startNum = fillTop(matrix, i, i, n-1-i, startNum)
            matrix, startNum = fillRight(matrix, i+1, n-2, n-1-i, startNum)
            matrix, startNum = fillBottom(matrix, n-1-i, i, n-1-i, startNum)
            matrix, startNum = fillLeft(matrix, i+1, i+1, i, startNum)
            
        # matrix, startNum = fillTop(matrix, 0, 0, n-1, 1)
        # # printMatrix(matrix)
        # matrix, startNum = fillRight(matrix, 1, 1, n-1, startNum)
        # # printMatrix(matrix)
        # matrix, startNum = fillBottom(matrix, n-1, 0, n-1, startNum)
        # # printMatrix(matrix)
        # matrix, startNum = fillLeft(matrix, 1, 1, 0, startNum)
        return matrix
'''

def fillTop(matrix, startRow, startCol, endCol, startNum):
    for i in range(startCol, endCol + 1):
        matrix[startRow][i] = startNum
        startNum += 1
    return matrix, startNum

def fillRight(matrix, startRow, endRow, endCol, startNum):
    for i in range(startRow, endRow + 1):
        matrix[i][endCol] = startNum
        startNum += 1
    return matrix, startNum

def fillBottom(matrix, startRow, startCol, endCol, startNum):
    for i in range(endCol, startCol - 1, -1):
        matrix[startRow][i] = startNum
        startNum += 1
    return matrix, startNum

def fillLeft(matrix, startRow, endRow, endCol, startNum):
    for i in range(endRow, startRow -1, -1):
        matrix[i][endCol] = startNum
        startNum += 1
    return matrix, startNum

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j] , end = ' ')
        print()

'''
# Solution 2
# Runtime: 36 ms, faster than 85.71% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for Spiral Matrix II.
class Solution(object):

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for i in range(n)]
        
        count = 1 
        i, j = 0, 0
        direction = 0
        circle = 0
        while count <= n*n:
            # print(i, j)
            matrix[i][j] = count
            count += 1
            
            if direction == 0:
                if j+1+circle == n:
                    direction = 1
                    i += 1
                else:
                    j += 1
            
            elif direction == 1:
                if i+1+circle == n:
                    direction = 2
                    j -= 1
                else:
                    i += 1
            
            elif direction == 2:
                if j-1-circle< 0:
                    direction = 3
                    i -= 1
                    circle += 1
                else:
                    j -= 1
            
            elif direction == 3:
                if i-1-circle < 0:
                    direction = 0
                    j += 1
                else:
                    i -= 1
        
        return matrix
'''

if __name__ == "__main__":
    n = 4
    sol = Solution()
    result = sol.generateMatrix(n)
    # result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    printMatrix(result)
    # print(3//2)