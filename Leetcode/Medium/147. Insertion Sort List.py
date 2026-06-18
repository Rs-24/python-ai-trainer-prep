

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Time: O(n^2)
        # Space: O(1)
        d = ListNode(0)
        c = head
        while c:
            t = d
            while t.next and t.next.val < c.val:
                t = t.next
            n = c.next
            c.next = t.next
            t.next = c
            c = n
        return d.next


