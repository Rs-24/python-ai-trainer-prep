# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/increasing-order-search-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(n), n = number of nodes in tree
        # Space, excluding output: O(h), h = height of tree, worst case O(n)
        # if tree skewed
        dummy = TreeNode()
        tail = dummy
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur.left = None
            tail.right = cur
            tail = tail.right
            cur = cur.right
        return dummy.right

# Recursive method:
from typing import Optional
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(n), n = number of nodes in tree
        # Space, excluding output: O(h) due to recursion stack, h = height of
        # tree, worst case O(n)
        dummy = TreeNode()
        tail = dummy
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal tail
            if node is None:
                return None
            dfs(node.left)
            node.left = None
            tail.right = node
            tail = tail.right
            dfs(node.right)
        dfs(root)
        return dummy.right


