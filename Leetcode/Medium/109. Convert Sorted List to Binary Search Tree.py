

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Time: O(n log n)
        # Space: O(log n)
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        t, s, f = None, head, head
        while f and f.next:
            t = s
            s = s.next
            f = f.next.next
        t.next = None
        r = TreeNode(s.val)
        r.left = self.sortedListToBST(head)
        r.right = self.sortedListToBST(s.next)
        return r


