

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Time: O(n)
        # Space: O(1)
        if not head or not head.next:
            return head
        o = head
        e = head.next
        eh = e
        while e and e.next:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next
        o.next = eh
        return head


