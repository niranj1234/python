# 16. 3Sum Closest

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 
# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans, n = nums[0] + nums[1] + nums[2], len(nums)
        for i in range(n):
            comp, j, k = target - nums[i], i + 1, n - 1
            while j < k:
                curr = nums[j] + nums[k] + nums[i]
                if abs(curr - target) < abs(ans - target):
                    ans = curr
                if nums[j] + nums[k] == comp:
                    return ans
                elif nums[j] + nums[k] > comp:
                    k -= 1
                else:
                    j += 1
        return ans
    
# Example usage:
solution = Solution()
nums = [-1, 2, 1, -4]
target = 1
result = solution.threeSumClosest(nums, target)
print(result)  # Output: 2