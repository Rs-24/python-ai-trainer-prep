

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Time: O(n)
        # Space: O(1)
        if head is None or head.next is None or k == 0:
            return head
        n = 1
        t = head
        while t.next:
            t = t.next
            n += 1
        t.next = head
        nt = head
        k %= n
        for _ in range(n - k - 1):
            nt = nt.next
        nh = nt.next
        nt.next = None
        return nh


