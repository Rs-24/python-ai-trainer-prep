

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(n)
        def dfs(n, c):
            if not n:
                return 0
            c = c * 10 + n.val
            if not n.left and not n.right:
                return c
            return dfs(n.left, c) + dfs(n.right, c)
        return dfs(root, 0)


