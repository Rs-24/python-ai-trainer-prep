# Time to write all of below including tests, explanation and time and aux 
# space: 15 mins

# Problem: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

if __name__ == "__main__":
    sol = Solution()
    assert sol.minDepth(None) == 0
    assert sol.minDepth(TreeNode(1)) == 1
    assert sol.minDepth(TreeNode(1, TreeNode(2))) == 2
    assert sol.minDepth(TreeNode(1, TreeNode(2), TreeNode(3))) == 2
    assert sol.minDepth(TreeNode(-1, TreeNode(0, None, TreeNode(1)), TreeNode(2))) == 2

# Explanation: the code uses a breadth-first-search method using a queue of 
# node, depth pairs, and returns the depth of the first node with no children
# Time: O(k), k = number of nodes processed before first leaf node reached,
# worst case O(n)
# Space: worst case O(w) extra due to queue, w = max width of tree


