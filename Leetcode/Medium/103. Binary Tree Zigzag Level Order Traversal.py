

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list]:
        if not root:
            return []
        out = []
        q = deque([root])
        lr = True
        while q:
            t = deque()
            for _ in range(len(q)):
                n = q.popleft()
                if lr:
                    t.append(n.val)
                else:
                    t.appendleft(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            out.append(list(t))
            lr = not lr
        return out


