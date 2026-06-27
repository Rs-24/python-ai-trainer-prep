

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        s = []
        while root or s:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


