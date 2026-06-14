

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Time: O(n)
        # Space: O(1)
        d = ListNode(0)
        d.next = head
        t = d
        while t.next and t.next.next:
            f, s = t.next, t.next.next
            f.next = s.next
            s.next = f
            t.next = s
            t = f
        return d.next


