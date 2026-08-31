

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        self.i = 0
        def b(x = float("inf")) -> TreeNode:
            if self.i == len(preorder) or preorder[self.i] > x:
                return None
            n = TreeNode(preorder[self.i])
            self.i += 1
            n.left = b(n.val)
            n.right = b(x)
            return n
        return b()


