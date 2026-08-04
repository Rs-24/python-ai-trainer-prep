

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(n)
        a = 0
        def dfs(n: TreeNode) -> int:
            nonlocal a
            if not n:
                return 0
            l = dfs(n.left)
            r = dfs(n.right)
            a += abs(l) + abs(r)
            return n.val + l + r - 1
        dfs(root)
        return a


