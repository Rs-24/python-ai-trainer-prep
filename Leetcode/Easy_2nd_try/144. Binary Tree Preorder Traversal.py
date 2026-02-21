# Time to write all of below including tests, explanation and time and aux 
# space: 21 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        out = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            out.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.preorderTraversal(None) == []
    assert sol.preorderTraversal(TreeNode(1)) == [1]
    assert sol.preorderTraversal(TreeNode(-1, TreeNode(0), TreeNode(1))) == [-1, 0, 1]
    assert sol.preorderTraversal(TreeNode(1, TreeNode(2, TreeNode(3)))) == [1, 2, 3]
    assert sol.preorderTraversal(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))) == [1, 2, 3]

# Explanation: the code uses a depth-first-search method using a stack and
# appends each node value to out before moving onto the left and right nodes
# Time: O(n), n = number of nodes in tree
# Space: excluding output: O(h), h = height of tree, worst case O(n) if tree
# skewed

# Learning lessons (done after completing all of above in 21 mins):
#   - Additionally, it would be useful to know the recursive depth-first-search
#     version. My attempt is below:
#
# def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     # Time: O(n), n = number of nodes in tree
#     # Space: excluding output: O(h) due to recursion stack, h = height of
#     # tree, worst case O(n) if tree skewed
#     out = []
#     def dfs(node: Optional[TreeNode]) -> None:
#         if not node:
#             return None
#         out.append(node.val)
#         dfs(node.left)
#         dfs(node.right)
#     dfs(root)
#     return out
#
#   - Additionally, another method is an iterative one but with a stack
#     consisting of (node, visited) pairs. My attempt is below:
#
# def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     # Time: O(n), n = number of nodes in tree
#     # Space: excluding output: O(h), h = height of tree, worst case O(n) if
#     # tree skewed
#     out = []
#     stack = [(root, False)]
#     while stack:
#         node, visited = stack.pop()
#         if not node:
#             continue
#         if visited:
#             out.append(node.val)
#         else:
#             stack.append((node.right, False))
#             stack.append((node.left, False))
#             stack.append((node, True))
#     return out



