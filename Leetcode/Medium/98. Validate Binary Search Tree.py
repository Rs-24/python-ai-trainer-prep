# Time to write all of below including tests, explanation and time and aux
# and total space: 1h 48 mins

# Problem: https://leetcode.com/problems/validate-binary-search-tree/description/

from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_max(node: Optional[TreeNode]) -> int:
            if not node:
                return -(2**31)
            else:
                return max(node.val, check_max(node.left), check_max(node.right))
        def check_min(node: Optional[TreeNode]) -> int:
            if not node:
                return 2**31 - 1
            else:
                return min(node.val, check_min(node.left), check_min(node.right))
        def check_valid(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            cur = check_max(node.left) < node.val < check_min(node.right)
            left = check_valid(node.left) 
            right = check_valid(node.right)
            return cur and left and right
        return check_valid(root)

if __name__ == "__main__":
    sol = Solution()
    assert sol.isValidBST(TreeNode(1)) == True
    assert sol.isValidBST(TreeNode(0, TreeNode(-1), TreeNode(1))) == True
    assert sol.isValidBST(TreeNode(1, TreeNode(2))) == False
    assert sol.isValidBST(TreeNode(0, TreeNode(-1, None, TreeNode(1)))) == False

# Explanation: the code uses recursion to check if every node has a valid left
# and right subtree by finding the max value in the left substree, and min value
# in the right subtree
# Time: O(n^2), n = number of nodes in tree
# Aux space, excluding output and input: O(h), h = height of tree, due to
# recursion stack
# Total space, including output, excluding input: O(h)

# Learning lessons (done after completing all of above in 1h 48 mins):
#   - I now realise there is a faster O(n) solution, my rewrite is below:
#
# def isValidBST(self, root: Optional[TreeNode]) -> bool:
#     # Time: O(n), n = number of nodes in tree
#     # Aux space, excluding output and input: O(h), h = height of tree, due to
#     # recursion stack
#     # Total space, including output, excluding input: O(h)
#     def dfs(node, low, high) -> bool:
#         if not node:
#             return True
#         if not (low < node.val < high):
#             return False
#         return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
#     return dfs(root, float("-inf"), float("inf"))
#
#   - Additionally, there is also another method using inorder traversal, my
#     attempt is below:
#
# def isValidBST(self, root: Optional[TreeNode]) -> bool:
#     # Time: O(n), n = number of nodes in tree
#     # Aux space, excluding output and input: O(h), h = height of tree, worst 
#     # case O(n) if tree skewed
#     # Total space, including output, excluding input: O(h), worst case O(n)
#     # if tree skewed
#     stack = []
#     prev = None
#     node = root
#     while node or stack:
#         while node:
#             stack.append(node)
#             node = node.left
#         node = stack.pop()
#         if prev is not None and prev >= node.val:
#             return False
#         prev = node.val
#         node = node.right
#     return True
#
#   - Additionally, my tests could have been improved. My rewrite is below: 
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.isValidBST(TreeNode(1)) == True
#     assert sol.isValidBST(TreeNode(0, TreeNode(-1), TreeNode(1))) == True
#     assert sol.isValidBST(TreeNode(1, TreeNode(2))) == False
#     assert sol.isValidBST(TreeNode(1, TreeNode(1))) == False
#     assert sol.isValidBST(TreeNode(0, TreeNode(-1, None, TreeNode(1)))) == False





