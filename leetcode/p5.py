# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/
# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    
    # def expandAroundCenter(self, s, left, right):
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left -= 1
    #         right += 1
    #     return right - left - 1

solution = Solution()

s = "babad"
result = solution.longestPalindrome(s)
print(result)  # Output: "bab" or "aba"
s = "cbbd"
result = solution.longestPalindrome(s)
print(result)  # Output: "bb"