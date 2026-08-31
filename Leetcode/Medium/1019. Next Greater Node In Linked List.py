

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> list:
        # Time: O(n)
        # Space: O(n)
        l, t = [], head
        while t:
            l.append(t.val)
            t = t.next
        a, s = [0] * len(l), []
        for i, x in enumerate(l):
            while s and l[s[-1]] < x:
                a[s.pop()] = x
            s.append(i)
        return a


