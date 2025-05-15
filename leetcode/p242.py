# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a , b = list(s), list(t)

        a.sort()
        b.sort()

        if (a==b):
            return True
        else:
            return False
