# Time to write all of below including tests, explanation and time and aux 
# space: 10 mins

# Problem: https://leetcode.com/problems/binary-tree-postorder-traversal/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        stack = [(root, False)]
        while stack:
            node, visited_children = stack.pop()
            
            if visited_children: 
                out.append(node.val)
                continue

            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.postorderTraversal(None) == []
    assert sol.postorderTraversal(TreeNode(1)) == [1]
    assert sol.postorderTraversal(TreeNode(1, TreeNode(-1), TreeNode(0))) == [-1, 0, 1]
    
# Explanation: The function iterates over the tree using a depth-first-search
# approach using a stack of (node, visited_children) pairs, and once the stack 
# is empty returns the variable 'out'
# Time: O(n), n = number of nodes in tree
# Aux space, excluding output and input: O(h), h = height of tree, worst case 
# O(n) if tree skewed
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 10 mins):
#   - It would be useful to know the recursive depth-first-search version, my
#     attempt is below:
#
# def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     # Time: O(n), n = number of nodes in tree
#     # Aux space, excluding output and input: O(h), h = height of tree due to 
#     # recursion stack, worst case O(n) if tree skewed
#     # Total space including output, excluding input: O(n)
#     out = []
#     def dfs(node: Optional[TreeNode]) -> None:
#         if not node:
#             return
#         dfs(node.left)
#         dfs(node.right)
#         out.append(node.val)
#     dfs(root)
#     return out
#
#   - Additionally, there is also an iterative method using a last_visited
#     pointer instead of a visited flag like in my origial solution. My attempt
#     is below:
#
# def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#     # Time: O(n), n = number of nodes in tree
#     # Aux space, excluding output and input: O(h), h = height of tree, worst
#     # case O(n) if tree skewed
#     # Total space, including output, excluding input: O(n)
#     out = []
#     stack = []
#     last_visited = None
#     cur = root
#     while cur or stack:        
#         if cur:
#             stack.append(cur)
#             cur = cur.left
#         else:
#             top = stack[-1]
#             if top.right is not None and last_visited is not top.right:
#                 cur = top.right
#             else:
#                 out.append(top.val)
#                 last_visited = stack.pop()
#     return out









        









