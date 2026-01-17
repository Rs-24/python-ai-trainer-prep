# Time to write all of below including tests, explanation and time and aux 
# space: 18 mins

# Problem: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root, 1])
        while q:
            length = len(q)
            for _ in range(length):
                node, depth = q.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.append((node.left, depth + 1))
                if node.right:
                    q.append((node.right, depth + 1))

# Tests:
# [] -> 0
# [1] -> 1
# [-1, 0, 1] -> 2

# Explanation: A breadth-first-search approach is used with a queue, where
# every node at each level is checked if they have any children and if not, 
# that depth is returned
# Time: O(n), n = number of nodes in tree
# Aux space: O(w), w = max number of nodes at any level reached before 
# finding a node with no children. Worst case O(n)
 
# Learning lessons (done after completing all of above in 18 mins):
#   - The line "q = deque([root, 1])" should actually be "q = deque([(root, 1)])"
#     for the program to work
#   - Also the code block:
#         length = len(q)
#         for _ in range(length):
#     is not necessary, and can be removed













