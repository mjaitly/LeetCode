'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

'''
# Brute Force - O(n2)

class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)
'''

'''
# Solution 2: with sorting O(n) 

def get_pivot(nums, low, high):
    mid = (low + high) // 2
    pivot = high
    if nums[low] < nums[mid]:
        if nums[mid] < nums[high]:
            pivot = mid
    elif nums[low] < nums[high]:
        pivot = low
    return pivot

def partition(nums, low, high):
    pivot_index = get_pivot(nums, low, high)
    pivot_value = nums[pivot_index]
    nums[pivot_index], nums[low] = nums[low], nums[pivot_index]
    border = low

    for i in range(low, high+1):
        if nums[i] < pivot_value:
            border += 1
            nums[i], nums[border] = nums[border], nums[i]
    nums[low], nums[border] = nums[border], nums[low]
    return border

def quick_sort(nums, low, high):
    if low<high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p-1)
        quick_sort(nums, p+1, high)
    return nums

def create_dict(nums, temp_nums):
    sorted_dict = {}
    for value in temp_nums:
        sorted_dict[value] = nums.index(value)
    return sorted_dict

class Solution:
    def twoSum(self, nums, target):
        temp_nums = nums[:]
        # Quick sort
        quick_sort(temp_nums, 0, len(nums)-1)
        # In-built sorting function
        # nums.sort()
        sorted_dict = create_dict(nums, temp_nums)
        keys = list(sorted_dict.keys())
        print(type(keys))
        for i in range(0, len(keys)):
            sum = keys[i] + keys[i+1]
            if sum == target:
                return [sorted_dict[keys[i]], sorted_dict[keys[i+1]]]


if __name__ == "__main__":
    nums = [2, 11, 7, 15]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)
'''

# Solution 3: one-pass O(n)
# Runtime: 56 ms, faster than 86.82% of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 12.09% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums, target):
        nums_dict = {}
        for i in range(0, len(nums)):
            if target - nums[i] in nums_dict:
                return [nums_dict[(target - nums[i])], i]
            else:
                nums_dict[nums[i]] = i

if __name__ == "__main__":
    nums = [2, 11, 7, 15]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)

