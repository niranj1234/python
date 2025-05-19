# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 
# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        lookup = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        letter_lists = []
        for ch in digits:
            letter_lists.append(lookup[ch])
            
        while len(letter_lists) > 1:
            l1 = letter_lists.pop()
            l2 = letter_lists.pop()
            combos = []
            for i in l1:
                for j in l2:
                    combos.append(j + i)
            letter_lists.append(combos)
            
        return [] if not letter_lists else letter_lists[0]
    
# Example usage:
solution = Solution()
digits = "23"
result = solution.letterCombinations(digits)
print(result)  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]