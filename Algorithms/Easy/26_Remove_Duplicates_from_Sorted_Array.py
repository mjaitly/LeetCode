'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
'''
# Runtime: 100 ms, faster than 55.30% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.5 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Time complextiy : O(n). Assume that nn is the length of array. Each of i and j traverses at most n steps.
# Space complexity : O(1).

class Solution:
    def removeDuplicates(self, nums) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                nums[index] = nums[i]
                index += 1
        print(nums)
        return index

if __name__ == "__main__":
    nums = [1,9,9,9,9,9,9,9,10,101]
    # nums = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    result = sol.removeDuplicates(nums)
    print(result)