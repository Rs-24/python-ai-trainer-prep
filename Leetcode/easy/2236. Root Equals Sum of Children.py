# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/root-equals-sum-of-children/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # Time: O(1)
        # Space: O(1)
        return root.val == root.left.val + root.right.val


