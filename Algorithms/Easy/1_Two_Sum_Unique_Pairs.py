'''
Given an int array nums and an int target, find how many unique pairs in the 
array such that their sum is equal to target. Return the number of pairs.
Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.
'''

class Solution:
    def twoSum(self, nums, target):
        pair_set = set()
        complement_set = set()
        for num in nums:
            complement = target - num
            if complement in complement_set:
                res = (num, complement) if num > complement else (complement, num)
                if res not in pair_set:
                    pair_set.add(res)
            complement_set.add(num)
        return len(pair_set)

if __name__ == "__main__":
    nums = [2, 11, 7, 15]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)