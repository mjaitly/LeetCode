'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1:
Input: [1,3,5,6], 5
Output: 2
'''

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target <= nums[0]:
            return 0
        for i in range(len(nums)-1):
            if target > nums[i] and target <= nums[i+1]:
                return i+1
        return len(nums)

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 0
    sol = Solution()
    result = sol.searchInsert(nums, target)
    print(result)

'''
# 45 ms
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = int((left + right)/2)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return left
'''
'''
# 40 ms
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] > target:
                right = mid - 1
                if nums[right] < target:
                    return right + 1
            elif nums[mid] < target:
                left = mid + 1
                if nums[left] > target:
                    return left
            else:
                return mid
'''