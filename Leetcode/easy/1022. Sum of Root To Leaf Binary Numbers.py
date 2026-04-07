# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h), h = height of tree, worst case O(n) if tree skewed
        stack = [(root, 0)]
        ans = 0
        while stack:
            node, total = stack.pop()
            if node is None:
                continue
            total = (total << 1) | node.val
            if node.left is None and node.right is None:
                ans += total
                continue
            stack.append((node.left, total))
            stack.append((node.right, total))
        return ans

# Recursive version:
from typing import Optional
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h) due to recursion stack, h = height of tree, worst case
        # O(n) if tree skewed
        def dfs(node: Optional[TreeNode], total_so_far) -> int:
            if node is None:
                return 0
            total_so_far <<= 1
            total_so_far |= node.val
            if node.left is None and node.right is None:
                return total_so_far
            return dfs(node.left, total_so_far) + dfs(node.right, total_so_far)
        return dfs(root, 0)


