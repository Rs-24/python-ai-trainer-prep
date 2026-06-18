

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Time: O(n)
        # Space: O(1)
        if not head or not head.next:
            return head
        m, t = head, head.next
        while t and t.next:
            m = m.next
            t = t.next.next
        l, r = head, m.next
        m.next = None
        l = self.sortList(l)
        r = self.sortList(r)
        d = ListNode()
        t = d
        while l and r:
            if l.val < r.val:
                t.next = l
                l = l.next
            else:
                t.next = r
                r = r.next
            t = t.next
        t.next = l or r
        return d.next


