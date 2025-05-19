# not finished
# 10. Regular Expression Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        special = [".","*"] 

        if(s == p):
            return True
        else:
            if(len(s) == len(p)):
                n = 0 
                while(n < len(s)):
                    
                    if(s[n] == p[n] or p[n] in special): 
                        n = n + 1
                    else:
                        return False
                        
                return True
            else:
                return False 
            

# Example usage:
solution = Solution()
# s = "aa"
# p = "a"
# result = solution.isMatch(s, p)     
# print(result)  # Output: False
# s = "aa"
# p = "a*"
# result = solution.isMatch(s, p)
# print(result)  # Output: True
# s = "ab"
# p = ".*"
# result = solution.isMatch(s, p)
# print(result)  # Output: True
s = "aab"
p = "c*a*b" 
result = solution.isMatch(s, p)
print(result)  # Output: True