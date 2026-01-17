# Time to write all of below including tests, explanation and time and aux 
# space: 15 mins

# Problem: https://leetcode.com/problems/path-sum/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q = deque([(root, root.val)])
        while q:
            node, sum = q.popleft()
            if sum == targetSum and not node.left and not node.right:
                return True
            if node.left:
                q.append((node.left, node.val + node.left.val))
            if node.right:
                q.append((node.right, node.val + node.right.val))
        return False

# Tests: 
# [], 0 -> False
# [], 1 -> False
# [1], 1 -> True
# [-1, 0, 1], 0 -> True
# [1, 2, 3], -1 -> False

# Explanation: A breadth-first-search method is used a queue containing each
# node and its corresponding sum. Each node is processed until a lead node is
# found with its sum equal to targetSum and True is returned. If no such node
# is found, then False is returned
# Time: O(n), n = number of nodes in tree
# Aux space: O(w), w = width of max level reached without a lead node summing
# to target, worst case O(n)

# Learning lessons (done after completing all of above in 15 mins):
#   - There is a bug, the lines:
#
#         if node.left:
#             q.append((node.left, node.val + node.left.val))
#         if node.right:
#             q.append((node.right, node.val + node.right.val))
#
#     should be:
#
#         if node.left:
#             q.append((node.left, sum + node.left.val))
#         if node.right:
#             q.append((node.right, sum + node.right.val))
#
#   - Also, the variable name 'sum' is also the name of an in-built python
#     function sum(). As such, it would be better to rename it to something
#     else like e.g. 'path_sum'


