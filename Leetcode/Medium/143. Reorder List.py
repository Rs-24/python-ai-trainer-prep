

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # Time: O(n)
        # Space: O(1)
        if not head or not head.next:
            return
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        p = None
        c = s.next
        s.next = None
        while c:
            t = c.next
            c.next = p
            p = c
            c = t
        f, s = head, p
        while s:
            t1 = f.next
            t2 = s.next
            f.next = s
            s.next= t1
            f = t1
            s = t2


