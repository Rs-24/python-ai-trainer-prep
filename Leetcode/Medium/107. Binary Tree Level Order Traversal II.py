

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list[list]:
        # Time: O(n)
        # Space: O(n)
        if not root:
            return []
        q = deque([root])
        out = deque()
        while q:
            t = []
            for _ in range(len(q)):
                n = q.popleft()
                t.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            out.appendleft(t)
        return list(out)


