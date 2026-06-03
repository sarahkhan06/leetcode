# Problem: Add Two Numbers — LeetCode #2
# Difficulty: Medium
# Pattern: Linked Lists
# Link: https://leetcode.com/problems/add-two-numbers/
# Time: O(max(m, n)) | Space: O(max(m, n))
#
# Intuition:
# Traverse both linked lists simultaneously, adding digits and managing carry.
# Build the result linked list digit by digit, just like manual addition.
#
# Approach:
# 1. Create a dummy node to anchor the result list
# 2. Iterate while either list has nodes or carry exists
# 3. Extract digits from current nodes (0 if list exhausted)
# 4. Calculate sum + carry, determine new carry and result digit
# 5. Create new node with result digit, move pointers forward
# 6. Return dummy.next (skip the dummy node)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# Key insight to remember:
# Process both lists in parallel, handle carry throughout.
# Dummy node simplifies result list construction.
