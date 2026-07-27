

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list:
        # Time: O(n)
        # Space: O(n)
        d = {}
        def dfs(n, p) -> None:
            if not n:
                return
            d[n] = p
            dfs(n.left, n)
            dfs(n.right, n)
        dfs(root, None)
        q = deque([(target, 0)])
        s = {target}
        a = []
        while q:
            n, t = q.popleft()
            if t == k:
                a.append(n.val)
                continue
            for nxt in [n.left, n.right, d[n]]:
                if nxt and nxt not in s:
                    s.add(nxt)
                    q.append((nxt, t + 1))
        return a


