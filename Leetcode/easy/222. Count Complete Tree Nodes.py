# Time to write all of below including tests, explanation and time and aux
# and total space: 23 mins

# Problem: https://leetcode.com/problems/count-complete-tree-nodes/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Time: O(h^2), h = height of tree = log n, n = number of nodes in tree
        # Space: O(h) due to recursion stack
        if root is None:
            return 0
        def left_height(node: Optional[TreeNode]) -> int:
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        def right_height(node: Optional[TreeNode]) -> int:
            h = 0
            while node:
                h += 1
                node = node.right
            return h
        lh = left_height(root)
        rh = right_height(root)
        if lh == rh:
            return (1 << lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        

