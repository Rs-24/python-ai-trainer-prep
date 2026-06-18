

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        # Time: O(n)
        # Space: O(1)
        if not root:
            return
        l = root
        while l.left:
            h = l
            while h:
                h.left.next = h.right
                if h.next:
                    h.right.next = h.next.left
                h = h.next
            l = l.left
        return root


