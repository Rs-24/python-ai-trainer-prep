# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h), h = height of tree, worst case O(n) if tree skewed
        stack = []
        cur = root
        prev_val = None
        best = float("inf")
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev_val is not None:
                best = min(best, abs(cur.val - prev_val))
            prev_val = cur.val
            cur = cur.right
        return best

# Recursive version:
from typing import Optional
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h) due to recursion stack, h = height of tree, worst case
        # O(n) if tree skewed
        prev_val = None
        best = float("inf")
        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal prev_val, best
            if node is None:
                return None
            inorder(node.left)
            if prev_val is not None:
                best = min(best, abs(node.val - prev_val))
            prev_val = node.val
            inorder(node.right)
        inorder(root)
        return best


