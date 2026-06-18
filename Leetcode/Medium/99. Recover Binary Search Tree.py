

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # Time: O(n)
        # Space: O(n)
        a = []
        f = s = p = None
        while root or a:
            while root:
                a.append(root)
                root = root.left
            root = a.pop()
            if p and p.val > root.val:
                if f is None:
                    f = p
                s = root
            p = root
            root = root.right
        f.val, s.val = s.val, f.val


