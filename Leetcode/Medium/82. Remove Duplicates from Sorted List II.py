

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Time: O(n)
        # Space: O(n)
        d = ListNode(0)
        t = d
        t.next = head
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                t.next = head.next
            else:
                t = t.next
            head = head.next
        return d.next


