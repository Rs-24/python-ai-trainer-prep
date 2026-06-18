

class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        # Time: O(n)
        # Space: O(n)
        if not head:
            return None
        d = {}
        c = head
        while c:
            d[c] = Node(c.val)
            c = c.next
        c = head
        while c:
            t = d[c]
            t.next = d.get(c.next)
            t.random = d.get(c.random)
            c = c.next
        return d[head]


