

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Time: O(n)
        # Space: O(n)
        ld = ListNode(0)
        gd = ListNode(0)
        l, g = ld, gd
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                g.next = head
                g = g.next
            head = head.next
        l.next = gd.next
        g.next = None
        return ld.next


