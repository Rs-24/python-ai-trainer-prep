

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        # Time: O(n)
        # Space: O(n)
        dummy = ListNode(0, head)
        d = {}
        s = 0
        cur = dummy
        while cur:
            s += cur.val
            d[s] = cur
            cur = cur.next
        s = 0
        cur = dummy
        while cur:
            s += cur.val
            cur.next = d[s].next
            cur = cur.next
        return dummy.next


