

from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # Time: O(n)
        # Space: O(n)
        d = defaultdict(int)
        d[0] = 1
        a = 0
        def dfs(n, c):
            nonlocal a
            if not n:
                return
            c += n.val
            a += d[c - targetSum]
            d[c] += 1
            dfs(n.left, c)
            dfs(n.right, c)
            d[c] -= 1
        dfs(root, 0)
        return a


