

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(n)
        q = deque([root])
        l, a, s = 1, 1, float("-inf")
        while q:
            t = 0
            for _ in range(len(q)):
                n = q.popleft()
                if n is not None:
                    t += n.val
                    q.append(n.left)
                    q.append(n.right)
            if t > s:
                a = l
                s = t
            l += 1
        return a


