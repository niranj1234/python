# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = len(height)
        a = 0
        b = l-1
        maxarea= 0
            
        while(a<b):   
            m = min(height[a], height[b]) 
            x=b-a
            maxarea = max(maxarea, m*x)
            if(height[a] <= height[b]):
                a+=1
            else:
                b-=1
        return maxarea   

# Example usage:
solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = solution.maxArea(height)
print(result)  # Output: 49


        