# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Time: O(n), n = number of nodes in tree
        # Space, excluding output: O(w), w = max number of nodes at any level
        out = []
        q = deque([root])
        while q:
            level_sum = 0
            width = len(q)
            for _ in range(width):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)                
            out.append(level_sum / width)
        return out


