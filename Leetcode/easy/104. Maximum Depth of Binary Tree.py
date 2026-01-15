# Time to write all of below including tests, explanation and time and aux 
# space: 15 mins

# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        q = deque([root])
        while q:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        return depth

if __name__ == "__main__":
    tests = [(TreeNode(-1, TreeNode(0), TreeNode(1)), 2), (None, 0), (TreeNode(1, TreeNode(2)), 2)]
    sol = Solution()
    for root, expected in tests:
        assert sol.maxDepth(root) == expected

# Explanation: a breadth-first-search method is used, and per level processed,
# depth is incremented
# Time: O(n)
# Aux space: O(n)

# Learning lessons (done after completing all of above in 15 mins):
#   - It would be useful to also know recursive method, my attempt is below:
#
# def maxDepth(self, root: Optional[TreeNode]) -> int:
#     # Time: O(n)
#     # Aux space: O(h), due to recursion stack, worst case O(n)
#     if not root:
#         return 0
#     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
#
#
# Additionally, the iterative depth-first-search method would also be useful
# to know. My attempt is below:
#
# def maxDepth(self, root: Optional[TreeNode]) -> int:
#     # Time: O(n), n = number of nodes in tree
#     # Aux space: O(h), h = height of longest explored path, worst case O(n) if
#     # tree skewed 
#     if not root:
#         return 0
#     longest = 0
#     stack = [(root, 1)]
#     while stack:
#         node, depth = stack.pop()
#         longest = max(longest, depth)
#         if node.left:
#             stack.append((node.left, depth + 1))
#         if node.right:
#             stack.append((node.right, depth + 1))
#     return longest
        
        



