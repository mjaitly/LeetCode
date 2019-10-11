'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

# Solution 1 - O(1) space
# Runtime: 96 ms, faster than 23.55% of Python3 online submissions for Rotate Array.
# Memory Usage: 15.2 MB, less than 5.09% of Python3 online submissions for Rotate Array.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

class Solution:
    def rotateLeft(self, array, k):
        n = len(array)
        numSets = gcd(n, k)
        for i in range(numSets):
            j = i
            temp = array[i]
            while 1:
                d = (j + k) % n # d = (j - k) % n for right rotate
                if d == i:
                    break
                array[j] = array[d]
                j = d
            array[j] = temp
        return array


if __name__ == "__main__":
    sol = Solution()
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    newArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 2
    result = sol.rotateLeft(array, k)
    print(result)
    # newArray = newArray[k:] + newArray[:k] # left rotate
    # newArray = newArray[len(array)-k:] + newArray[:len(array)-k] # right rotate
    # print(newArray)
