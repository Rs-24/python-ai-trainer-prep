

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        # Time: O(n)
        # Space: O(n)
        if not node:
            return None
        s = {}
        def dfs(n):
            if n in s:
                return s[n]
            c = Node(n.val)
            s[n] = c
            for nb in n.neighbors:
                c.neighbors.append(dfs(nb))
            return c
        return dfs(node)


