

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Time: O(n)
        # Space: O(n)
        d = ListNode()
        t = d
        c = 0
        while l1 or l2 or c:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            t.next = ListNode((x + y + c) % 10)
            t = t.next
            c = (x + y + c) // 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return d.next


