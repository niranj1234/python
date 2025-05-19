# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        dups = set()
        seen = dict()

        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j in range(i + 1, len(nums)):
                    val2 = nums[j]
                    complement = -(val1 + val2)
                    if complement in seen and seen[complement] == i:
                        triplet = sorted([val1, val2, complement])
                        res.add(tuple(triplet))  # Use tuple for hashability

                    seen[val2] = i

        return [list(tri) for tri in res]
    
# Example usage:
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = solution.threeSum(nums)
print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]