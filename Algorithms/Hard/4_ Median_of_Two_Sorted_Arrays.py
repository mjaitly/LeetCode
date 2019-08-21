'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
'''
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)
        
        if n > m:
            nums1, n, nums2, m = nums2, m, nums1, n
        
        min_index = 0
        max_index = n

        while (min_index <= max_index): 
		
            i = (min_index + max_index) // 2
            j = ((n + m + 1) // 2) - i 
        
            # if i = n, it means that Elements 
            # from a[] in the second half is 
            # an empty set. If j = 0, it means 
            # that Elements from b[] in the first 
            # half is an empty set. so it is necessary 
            # to check that, because we compare elements 
            # from these two groups. searching on right 
            if (i < n and j > 0 and nums2[j - 1] > nums1[i]):	 
                min_index = i + 1	
            
            # if i = 0, it means that Elements from 
            # a[] in the first half is an empty set 
            # and if j = m, it means that Elements 
            # from b[] in the second half is an 
            # a[] in the first half is an empty set 
            # that, because we compare elements from 
            # these two groups. searching on left 
            elif (i > 0 and j < m and nums2[j] < nums1[i - 1]):	 
                max_index = i - 1	
            
            # we have found the desired halves. 
            else: 
                
                # this condition happens when we don't have 
                # any elements in the first half from a[] so 
                # we returning the last element in b[] from 
                # the first half. 
                if (i == 0): 
                    return nums2[j - 1]		 
                
                # and this condition happens when we don't 
                # have any elements in the first half from 
                # b[] so we returning the last element in 
                # a[] from the first half. 
                if (j == 0): 
                    return nums1[i - 1]		 
                else: 
                    return max(nums1[i - 1], nums2[j - 1]) 

        print("ERROR!!! " , "returning\n")
        return 0

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(result)
'''
# Solution 1: 
# Runtime: 100 ms, faster than 95.39% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left
                
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(result)