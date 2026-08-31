

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(n)
        def dfs(n: TreeNode, parent_val: int, grandparent_val: int) -> int:
            if not n:
                return 0
            l = dfs(n.left, n.val, parent_val)
            r = dfs(n.right, n.val, parent_val)
            return n.val + l + r if grandparent_val % 2 == 0 else l + r
        return dfs(root, 1, 1)


