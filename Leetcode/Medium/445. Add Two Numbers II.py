

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Time: O(n)
        # Space: O(n)
        a, b = [], []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        c, o = 0, None
        while a or b or c:
            x = a.pop() if a else 0
            y = b.pop() if b else 0
            t = x + y + c
            c = t // 10
            n = ListNode(t % 10)
            n.next = o
            o = n
        return o


