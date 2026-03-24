# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/subtree-of-another-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time: O(m * n), m = number of nodes in root, n = number of
        # nodes in subRoot
        # Space: O(h_m + h_n) due to recursion stack, h_m = height
        # of root, h_n = height of subRoot, worst case O(m + n) if
        # both trees skewed
        if root is None:
            return False
        def is_same(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            l = is_same(root1.left, root2.left)
            r = is_same(root1.right, root2.right)
            return root1.val == root2.val and l and r
        return is_same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        