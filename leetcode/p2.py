# 2. Add Two Numbers
# # LeetCode Problem 2
# # Problem URL: https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l= ""
        t =""
        x = 0
        a=[]
        while l1:
            l=str(l1.val)+l
            l1 = l1.next

        while l2:
            t = str(l2.val)+t
            l2 = l2.next


        x = int(l) +int(t)

        y = str(x)[::-1]
        
        d = ListNode()
        c = d

        for k in y:
            c.next = ListNode(int(k))
            c = c.next
            
        return d.next


# Example usage:   
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")
# Output: 7 -> 0 -> 8 -> None
