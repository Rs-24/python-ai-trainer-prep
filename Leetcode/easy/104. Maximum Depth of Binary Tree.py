# Time to write all of below including tests, explanation and time and aux 
# space: 7 mins

# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        best = 0
        while stack:
            node, depth = stack.pop()
            if node is None:
                continue
            best = max(best, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
        return best

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxDepth(None) == 0
    assert sol.maxDepth(TreeNode(1)) == 1
    assert sol.maxDepth(TreeNode(-1, TreeNode(0), TreeNode(1))) == 2
    assert sol.maxDepth(TreeNode(1, TreeNode(2), TreeNode(2, TreeNode(3)))) == 3

# Explanation: the code uses a depth-first-search approach using a stack to
# find the depth of each node and returns the maximum depth reached
# Time: O(n), n = number of nodes in tree
# Space: O(h), h = height of tree, worst case O(n) if tree skewed
        
# Iterative breadth-first-search method:
from collections import deque
def maxDepth(self, root: Optional[TreeNode]) -> int:
    # Time: O(n), n = number of nodes in tree
    # Space: O(w), w = max width of tree
    q = deque([(root, 1)])
    best = 0
    while q:
        node, depth = q.popleft()
        if node is None:
            continue
        best = max(best, depth)
        q.append((node.left, depth + 1))
        q.append((node.right, depth + 1))
    return best

# Recursive method:
def maxDepth(self, root: Optional[TreeNode]) -> int:
    # Time: O(n), n = number of nodes in tree
    # Space: O(h) due to recursion stack, h = height of tree, worst case O(n)
    # if tree skewed
    if not root:
        return 0
    l = self.maxDepth(root.left)
    r = self.maxDepth(root.right)
    return 1 + max(l, r)


