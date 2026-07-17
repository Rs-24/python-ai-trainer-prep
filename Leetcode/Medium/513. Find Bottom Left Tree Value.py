

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(n)
        q = deque([root])
        a = root.val
        while q:
            t = len(q)
            a = q[0].val
            for _ in range(t):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return a


