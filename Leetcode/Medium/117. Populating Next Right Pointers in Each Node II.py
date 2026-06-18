

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
            return None
        c = root
        while c:
            d = Node(0)
            t = d
            while c:
                if c.left:
                    t.next = c.left
                    t = t.next
                if c.right:
                    t.next = c.right
                    t = t.next
                c = c.next
            c = d.next
        return root


