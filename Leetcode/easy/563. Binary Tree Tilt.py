# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/binary-tree-tilt/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h) due to recursion stack, h = height of tree, worst case
        # O(n) if tree skewed
        total = 0
        def sum_nodes(node: Optional[TreeNode]) -> int:
            nonlocal total
            if node is None:
                return 0
            ls = sum_nodes(node.left)
            rs = sum_nodes(node.right)
            total += abs(ls - rs)
            return node.val + ls + rs
        sum_nodes(root)
        return total


