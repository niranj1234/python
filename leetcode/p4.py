# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a=nums1+nums2
        a.sort()
        z = len(a)
        if (len(a)%2 == 0):
            d = len(a)//2
            s= sum(a[d-1:d+1])/2
        else:
            x = len(a)//2
            s= float(a[x])
        return s
# Example usage:
solution = Solution()
nums1 = [1, 3]
nums2 = [2]
result = solution.findMedianSortedArrays(nums1, nums2)
print(f"{result:.5f}")  # Output: 2.00000
# Example usage:
nums1 = [1, 2]
nums2 = [3, 4]
result = solution.findMedianSortedArrays(nums1, nums2)
print(f"{result:.5f}")  # Output: 2.50000