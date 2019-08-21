'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.
'''
'''
# Solution 1: Two Pointers
# Runtime: 44 ms, faster than 32.06% of Python3 online submissions for Remove Element.
# Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums, val: int) -> int:
        index = 0
        if not nums:
            return 0
        else:
            for i in range(0, len(nums)):
                if nums[i] != val:
                    nums[index] = nums[i]
                    index += 1
        print(nums)
        return index


if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    sol = Solution()
    result = sol.removeElement(nums, val)
    print(result)
'''
# Solution 2: Two Pointers - when elements to remove are rare
# Runtime: 40 ms, faster than 69.73% of Python3 online submissions for Remove Element.
# Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions for Remove Element.

class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        n = len(nums)
        if not nums:
            return 0
        else:
            while i < n:
                if nums[i] == val:
                    nums[i] = nums[n-1]
                    n -= 1
                else:
                    i += 1
        return i


if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    sol = Solution()
    result = sol.removeElement(nums, val)
    print(result)