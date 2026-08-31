

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        def dfs(n: TreeNode, r: int):
            if not n:
                return None
            r -= n.val
            if not n.left and not n.right:
                return n if r <= 0 else None
            n.left = dfs(n.left, r)
            n.right = dfs(n.right, r)
            if not n.left and not n.right:
                return None
            return n
        return dfs(root, limit)


