# Time to write all of below including tests, explanation and time and aux
# and total space: 16 mins

# Problem: https://leetcode.com/problems/binary-tree-paths/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Time: O(n * h), n = number of nodes in tree, h = height of tree 
        # Space, excluding output: O(h), worst case O(n) if tree skewed
        if not root:
            return []
        out = []
        stack = [(root, [str(root.val)])]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                out.append("".join(path))
            path.append("->")
            if node.left:
                stack.append((node.left, path + [str(node.left.val)]))
            if node.right:
                stack.append((node.right, path + [str(node.right.val)]))
        return out

# Recursive method:
from typing import List, Optional
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Time: O(n * h), n = number of nodes in tree, h = height of tree
        # Space, excluding output: O(h) due to recursion stack,
        # worst case O(n) if tree skewed
        if not root:
            return []
        out = []
        def dfs(node: Optional[TreeNode], path: List[str]) -> None:
            if not node.left and not node.right:
                out.append("".join(path))
            if node.left:
                dfs(node.left, path + ["->", str(node.left.val)])
            if node.right:
                dfs(node.right, path + ["->", str(node.right.val)])
        dfs(root, [str(root.val)])
        return out


