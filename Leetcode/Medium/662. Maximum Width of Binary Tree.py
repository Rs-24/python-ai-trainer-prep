

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(n)
        if not root:
            return 0
        q = deque([(root, 0)])
        a = 0
        while q:
            t = len(q)
            i = q[0][1]
            for j in range(t):
                n, k = q.popleft()
                k -= i
                if j == t - 1:
                    a = max(a, k + 1)
                if n.left:
                    q.append((n.left, 2 * k))
                if n.right:
                    q.append((n.right, 2 * k + 1))
        return a


