

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set(nums)
        a = 0
        while head:
            a += head.val in s and (head.next is None or head.next.val not in s)
            head = head.next
        return a


