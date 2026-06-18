

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Time: O(n)
        # Space: O(1)
        if not head or not head.next:
            return None
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                s = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        return None


