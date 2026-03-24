# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h) due to recursion stack, h = height of tree, worst case
        # O(n) if tree skewed
        def preorder(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            if node.val > root.val:
                return node.val
            l = preorder(node.left)
            r = preorder(node.right)
            if l == -1:
                return r
            if r == -1:
                return l
            return min(l, r)
        return preorder(root)

# set version:
from typing import Optional
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # Time: O(n log n), n = number of nodes in tree
        # Space: O(n)
        seen = set()
        def preorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return None
            seen.add(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        nums = sorted(seen)
        return nums[1] if len(nums) > 1 else -1


