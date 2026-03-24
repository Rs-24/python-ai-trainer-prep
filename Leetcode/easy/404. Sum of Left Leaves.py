# Time to write all of below including tests, explanation and time and aux
# and total space: 15 mins

# Problem: https://leetcode.com/problems/sum-of-left-leaves/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(w), w = max number of nodes at any level (max width)
        total = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                continue
            if node.left is not None and node.left.left is None and node.left.right is None:
                total += node.left.val
            q.append(node.left)
            q.append(node.right)
        return total

# Recursive method: 
from typing import Optional
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Time: O(n), n = number of nodes in tree
        # Space: O(h), h = height of tree, worst case O(n) if tree skewed
        if root is None:
            return 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


