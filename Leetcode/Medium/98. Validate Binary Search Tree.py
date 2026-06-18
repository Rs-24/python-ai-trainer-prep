

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Time: O(n)
        # Space: O(n)
        s = [(root, float("-inf"), float("inf"))]
        while s:
            n, l, h = s.pop()
            if not n:
                continue
            if not (l < n.val < h):
                return False
            s.append((n.left, l, n.val))
            s.append((n.right, n.val, h))
        return True


