# Time to write all of below including tests, explanation and time and aux 
# space: 14 mins

# Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            out.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.preorderTraversal(None) == []
    assert sol.preorderTraversal(TreeNode(1)) == [1]
    assert sol.preorderTraversal(TreeNode(-1, TreeNode(0), TreeNode(1))) == [-1, 0, 1]
   
# Explanation: The function iterates over the tree via a depth-first-search
# approach, and first appends the node value itself to out, then moves onto the 
# left node, then the right node
# Time: O(n), n = number of nodes in the tree
# Aux space, excluding output and input: O(h), h = height of tree, worst case O(n)
# if tree skewed
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 14 mins):
#   - The "if not node: continue" code block isn't necessary because None is 
#     never pushed anyway. As such, it can be removed
#   - Additionally, it would be useful to know the recursive depth-first-search
#     version. My attempt is below:
#
# def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     # Time: O(n), n = number of nodes in tree
#     # Aux space, excluding output and input: O(h), h = height of tree, due to
#     # recursion stack, worst case O(n) if tree skewed
#     # Total space, including output, excluding input: O(n)
#     out = []
#     def dfs(node: Optional[TreeNode]) -> None:
#         if not node:
#             return
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
#     # Aux space, excluding output and input: O(h), h = height of tree, 
#     # worst case O(n) if tree skewed
#     # Total space, including output, excluding input: O(n)
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





    













