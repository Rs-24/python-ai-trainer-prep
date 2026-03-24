# Time to write all of below including tests, explanation and time and aux
# and total space: 11 mins

# Problem: https://leetcode.com/problems/merge-two-binary-trees/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(m + n), m = number of nodes in root1, n = number of
        # nodes in root2
        # Space: O(max(h_1, h_2)) due to recursion stack, h_1 = height of root1,
        # h_2 = height of root2, worst case O(max(m, n)) if trees skewed  
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

# Iterative breadth-first-search version:
from typing import Optional
from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(m + n), m = number of nodes in root1, n = number of
        # nodes in root2
        # Space: O(max(w_1, w_2)), w_1 = width of root1, w_2 = width of root2
        if not root1:
            return root2
        if not root2:
            return root1    
        q = deque([(root1, root2)])
        while q:
            a, b = q.popleft()
            a.val += b.val
            if a.left and b.left:
                q.append((a.left, b.left))
            elif a.left is None:
                a.left = b.left
            if a.right and b.right:
                q.append((a.right, b.right))
            elif a.right is None:
                a.right = b.right
        return root1


