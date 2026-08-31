

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(n)
        def dfs(n: TreeNode, l: int, h: int):
            if not n:
                return h - l
            l = min(l, n.val)
            h = max(h, n.val)
            return max(dfs(n.left, l, h), dfs(n.right, l, h))
        return dfs(root, root.val, root.val)


