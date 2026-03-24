# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/search-in-a-binary-search-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Time: O(h), h = height of tree
        # Space: O(1)
        cur = root
        while cur:
            if cur.val == val:
                return cur
            elif cur.val < val:
                cur = cur.right
            else:
                cur = cur.left       
        return None

# Recursive method:
from typing import Optional
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Time: O(h), h = height of tree
        # Space: O(h) due to recursion stack, worst case O(n) if tree skewed
        if root is None or root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)


