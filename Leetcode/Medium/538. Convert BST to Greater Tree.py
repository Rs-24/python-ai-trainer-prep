

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        s = 0
        def dfs(n):
            nonlocal s
            if not n:
                return
            dfs(n.right)
            s += n.val
            n.val = s
            dfs(n.left)
        dfs(root)
        return root


