# Time to write all of below including tests, explanation and time and aux 
# space: 29 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/balanced-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [(root, False)]
        height = {None: 0}
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                lh = height[node.left]
                rh = height[node.right]
                if abs(lh - rh) > 1:
                    return False
                height[node] = 1 + max(lh, rh)
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isBalanced(None) == True
    assert sol.isBalanced(TreeNode(1)) == True
    assert sol.isBalanced(TreeNode(1, TreeNode(2))) == True
    assert sol.isBalanced(TreeNode(-1, TreeNode(0), TreeNode(1))) == True
    assert sol.isBalanced(TreeNode(1, TreeNode(2, None, TreeNode(3)))) == False
    assert sol.isBalanced(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4))) == True

# Explanation: the code uses an iterative depth-first-search approach with a
# stack and checks the height of the left and right child of each node using
# a dictionary which stores the height of each node
# Time: O(n), n = number of nodes in tree
# Space: worst case O(n) extra due to height dictionary

# Learning lessons (done after completing all of above in 29 mins):
#   - It would be useful to know the recursive method, my attempt is below:
#
# def isBalanced(self, root: Optional[TreeNode]) -> bool:
#     # Time: worst case O(n), n = number of nodes in tree
#     # Space: O(h) due to recursion stack, h = max height reached
#     def height(node: Optional[TreeNode]) -> int:
#         if node is None:
#             return 0
#         lh = height(node.left)
#         rh = height(node.right)
#         if lh == -1 or rh == -1 or abs(lh - rh) > 1:
#             return -1 
#         return 1 + max(lh, rh)
#     return height(root) != -1




