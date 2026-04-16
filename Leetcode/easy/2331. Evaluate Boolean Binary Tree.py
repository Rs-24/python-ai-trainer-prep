# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/evaluate-boolean-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h) due to recursion stack, h = height of tree, worst case O(n)
        # if tree skewed
        if root.val == 0 or root.val == 1:
            return root.val
        elif root.val == 2:
            return self.evaluateTree(root.left) | self.evaluateTree(root.right)
        return self.evaluateTree(root.left) & self.evaluateTree(root.right)


