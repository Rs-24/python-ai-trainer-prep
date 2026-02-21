# Time to write all of below including tests, explanation and time and aux 
# space: 16 mins

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
        if root is None:
            return False
        stack = [(root, root.val)]
        while stack:
            node, total = stack.pop()
            if total == targetSum and not node.left and not node.right:
                return True
            if node.left:
                stack.append((node.left, total + node.left.val))
            if node.right:
                stack.append((node.right, total + node.right.val))
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.hasPathSum(None, 1) == False
    assert sol.hasPathSum(TreeNode(1), 1) == True
    assert sol.hasPathSum(TreeNode(1), 2) == False
    assert sol.hasPathSum(TreeNode(1, TreeNode(2)), 3) == True
    assert sol.hasPathSum(TreeNode(-1, TreeNode(0), TreeNode(1)), 0) == True
    assert sol.hasPathSum(TreeNode(-1, TreeNode(-2), TreeNode(-3, TreeNode(1))), -1) == False

# Explanation: the code uses a depth-first-search approach using a stack of 
# node, total pairs, and if a leaf node is reached with total equal to 
# targetSum, True is returned. If the loop ends without having returned
# anything, then False is returned
# Time: O(k), k = number of nodes processed, worst case O(n),
# n = number of nodes in tree
# Space: O(h), h = max height reached, worst case O(n) if tree
# skewed

# Learning lessons (done after completing all of above in 16 mins):
#   - No major learning lessons


