# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/cousins-in-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h), h = height of tree, worst case O(n) if tree skewed
        stack = [(root, 0, None)]
        cousin_depth = None
        cousin_parent = None
        while stack:
            node, depth, parent = stack.pop()
            if node is None:
                continue
            if node.val == x or node.val == y:
                if cousin_depth is None:
                    cousin_depth = depth
                    cousin_parent = parent
                else:
                    if depth == cousin_depth and parent != cousin_parent:
                        return True
                    return False
            stack.append((node.left, depth + 1, node))
            stack.append((node.right, depth + 1, node))
        return False

# Recursive version:
from typing import Optional
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h) due to recursion stack, h = height of tree, worst case
        # O(n) if tree skewed
        x_depth = None
        x_parent = None
        y_depth = None
        y_parent = None
        def dfs(node: Optional[TreeNode], depth: int, parent: Optional[TreeNode]) -> None:
            nonlocal x_depth, x_parent, y_depth, y_parent
            if node is None:
                return None
            if node.val == x:
                x_depth = depth
                x_parent = parent
            if node.val == y:
                y_depth = depth
                y_parent = parent
            dfs(node.left, depth + 1, node)
            dfs(node.right, depth + 1, node)
        dfs(root, 0, None)
        return x_depth == y_depth and x_parent != y_parent


