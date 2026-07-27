

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        def dfs(n):
            if not n:
                return
            n.left = dfs(n.left)
            n.right = dfs(n.right)
            if n.val != 1 and n.left is None and n.right is None:
                return None
            return n
        return dfs(root)


