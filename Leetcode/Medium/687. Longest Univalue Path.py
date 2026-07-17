

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(n)
        a = 0
        def dfs(n):
            nonlocal a
            if not n:
                return 0
            l = dfs(n.left)
            r = dfs(n.right)
            lp = rp = 0
            if n.left and n.left.val == n.val:
                lp = l + 1
            if n.right and n.right.val == n.val:
                rp = r + 1
            a = max(a, lp + rp)
            return max(lp, rp)
        dfs(root)
        return a


