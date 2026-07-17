

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> list:
        # Time: O(n)
        # Space: O(n)
        if not root:
            return []
        a = []
        q = deque([root])
        while q:
            l = len(q)
            t = float("-inf")
            for _ in range(l):
                n = q.popleft()
                t = max(t, n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            a.append(t)
        return a


