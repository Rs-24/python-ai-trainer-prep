

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        # Time: O(n)
        # Space: O(n)
        if not root:
            return []
        out = []
        q = deque([root])
        while q:
            t = len(q)
            for i in range(t):
                n = q.popleft()
                if i == t - 1:
                    out.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return out


