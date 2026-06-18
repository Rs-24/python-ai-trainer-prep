

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        # Time: O(n)
        # Space: O(n)
        self.p = None
        def dfs(n):
            if not n:
                return
            dfs(n.right)
            dfs(n.left)
            n.right = self.p
            n.left = None
            self.p = n
        dfs(root)


