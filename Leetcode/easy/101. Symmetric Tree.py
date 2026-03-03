# Time to write all of below including tests, why the solution works and time 
# and space complexity: 14 mins

# Problem: https://leetcode.com/problems/symmetric-tree/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q = deque([(root.left, root.right)])
        while q:
            a, b = q.popleft()
            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            q.append((a.left, b.right))
            q.append((a.right, b.left))
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isSymmetric(TreeNode(1)) == True
    assert sol.isSymmetric(TreeNode(1, TreeNode(2))) == False
    assert sol.isSymmetric(TreeNode(1, TreeNode(2), TreeNode(2))) == True
    assert sol.isSymmetric(TreeNode(-1, TreeNode(0), TreeNode(1))) == False

# Explanation: the code uses a breadth-first-search method using a queue to
# determine if the tree is symmetrical by comparing the appropriate pairs
# Time: O(k), k = number of nodes compared, worst case O(n) if e.g.
# all nodes compared, n = number of nodes in tree
# Space: O(w), w = max width reached

# Recursive method:
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    # Time: O(k), k = number of nodes compared, worst case O(n) if e.g.
    # all nodes compared, n = number of nodes in tree
    # Space: O(h) due to recursion stack, h = max height reached, worst case
    # O(n) if tree skewed
    if root is None:
        return True
    def check(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return check(a.left, b.right) and check(a.right, b.left)
    return check(root.left, root.right)

# Iterative depth-first-search method:
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    # Time: O(k), k = number of nodes compared, worst case O(n) if e.g.
    # all nodes compared, n = number of nodes in tree
    # Space: O(h), h = max height reached, worst case O(n) if tree skewed
    if root is None:
        return True
    stack = [(root.left, root.right)]
    while stack:
        a, b = stack.pop()
        if not a and not b:
            continue
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        stack.append((a.left, b.right))
        stack.append((a.right, b.left))
    return True


