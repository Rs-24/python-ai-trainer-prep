# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/univalued-binary-tree/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n), n = number of nodes in tree
        # Space: O(w), w = max width of tree
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                continue
            if node.val != root.val:
                return False
            q.append(node.left)
            q.append(node.right)
        return True

# Recursive version:
from typing import Optional
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h) due to recursion stack, h = height of tree, worst case
        # O(n) if tree skewed
        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True
            return root.val == node.val and dfs(node.left) and dfs(node.right)
        return dfs(root)


