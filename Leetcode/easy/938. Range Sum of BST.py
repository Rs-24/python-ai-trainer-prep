# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/range-sum-of-bst/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h), h = height of tree, worst case O(n) if tree skewed
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if low <= node.val <= high:
                total += node.val
            if node.val > low:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)
        return total

# Recursive version:
from typing import Optional
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h) due to recursion stack, worst case O(n) if tree skewed
        if root is None:
            return 0
        cur = root.val if low <= root.val <= high else 0
        l = self.rangeSumBST(root.left, low, high) if root.val > low else 0
        r = self.rangeSumBST(root.right, low, high) if root.val < high else 0
        return cur + l + r


