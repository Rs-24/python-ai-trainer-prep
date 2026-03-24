# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/diameter-of-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h) due to recursion stack, worst case O(n) if tree skewed
        best = 0
        def height(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            best = max(best, lh + rh)
            return 1 + max(lh, rh)
        height(root)
        return best


