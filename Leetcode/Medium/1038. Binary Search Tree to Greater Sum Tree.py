

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        self.t = 0
        def dfs(n: TreeNode) -> None:
            if not n:
                return
            dfs(n.right)
            self.t += n.val
            n.val = self.t
            dfs(n.left)
        dfs(root)
        return root


