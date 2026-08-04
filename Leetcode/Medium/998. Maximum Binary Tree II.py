

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        if root is None or root.val < val:
            n = TreeNode(val)
            n.left = root
            return n
        root.right = self.insertIntoMaxTree(root.right, val)
        return root


