# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # Time: O(n), n = number of nodes in linked list
        # Space: O(1)
        num = 0
        while head:
            num |= head.val
            num <<= 1
            head = head.next
        return num >> 1


