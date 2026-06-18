

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Time: O(n)
        # Space: O(n)
        if not head or left == right:
            return head
        d = ListNode(0)
        d.next = head
        prev = d
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next
        for _ in range(right - left):
            t = cur.next
            cur.next = t.next
            t.next = prev.next
            prev.next = t
        return d.next


