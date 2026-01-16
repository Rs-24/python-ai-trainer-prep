# Time to write all of below including tests, explanation and time and aux 
# space: 26 mins

# Problem: https://leetcode.com/problems/balanced-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            if not root.left:
                if not root.right.left and not root.right.right:
                    return True
                return False
            if not root.right:
                if not root.left.left and not root.left.right:
                    return True
                return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

# Tests:
# [] -> True
# [1] -> True
# [-1, 0, 1] -> True
# [1, 2, null] -> True
# [1, null, 2, null, 3] -> False

# Explanation: recursion is used for every node in the tree to determine if
# each node is balanced
# Time: O(n), n = number of nodes in tree
# Aux space: O(k), k = number of balanced nodes reached, worst case O(n)
#
# Learning lessons (done after completing all of above in 26 mins):
#   - I realise now my solution is flawed, e.g.
#          1
#         / \
#        2   3
#       / \
#      4   5
#     / \ / \
#    8  9 10 11
#     results in True, when it is actually false. As such, my rewrite is below:
#
# def isBalanced(self, root: Optional[TreeNode]) -> bool:
#     # Time: O(n), n = number of nodes in tree
#     # Aux space: O(h), h = height reached before imbalance due to recursion
#     # stack, worst case O(n) if tree skewed
#     def height(node: Optional[TreeNode]) -> int:
#         if not node:
#             return 0
#         lh = height(node.left)
#         if lh == -1:
#             return -1
#         rh = height(node.right)
#         if rh == -1:
#             return -1
#         if abs(lh - rh) > 1:
#             return -1
#         return 1 + max(lh, rh)
#     return height(root) != -1
#
# Additionally, it would be useful to know the iterative version. My attempt is
# below:
#
# def isBalanced(self, root: Optional[TreeNode]) -> bool:
#     # Time: O(n), n = number of nodes in tree
#     # Aux space: O(n)
#     if not root:
#         return True
#     stack = [(root, False)]
#     height = {None: 0}
#     while stack:
#         node, visited = stack.pop()
#         if not node:
#             continue
#         if not visited:
#             stack.append((node, True))
#             stack.append((node.left, False))
#             stack.append((node.right, False))
#         else:
#             lh = height[node.left]
#             rh = height[node.right]
#             if abs(lh - rh) > 1:
#                 return False
#             height[node] = 1 + max(lh, rh)
#     return True












