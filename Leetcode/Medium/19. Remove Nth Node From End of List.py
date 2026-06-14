

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Time: O(n)
        # Space: O(1)
        d = ListNode(0, head)
        f = s = d
        for _ in range(n + 1):
            f = f.next
        while f:
            f = f.next
            s = s.next
        s.next = s.next.next
        return d.next


