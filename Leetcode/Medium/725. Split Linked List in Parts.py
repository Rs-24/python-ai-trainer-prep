

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list:
        # Time: O(n)
        # Space: O(n)
        n = 0
        t = head
        while t:
            n += 1
            t = t.next
        o = []
        t = head
        for i in range(k):
            h = t
            s = (n // k) + (1 if i < (n % k) else 0)
            for _ in range(s - 1):
                if h:
                    h = h.next
            if h:
                x = t.next
                t.next = None
                t = x
            o.append(h)
        return o


