# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/leaf-similar-trees/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Time: O(m + n), m = number of nodes in root1, n = number of nodes in
        # root2
        # Space: O(h1 + h2), h1 = height of root1, h2 = height of root2, worst
        # case O(n + m) if both trees skewed
        def build(node1: Optional[TreeNode]) -> List[int]:
            out = []
            stack = [node1]
            while stack:
                a = stack.pop()
                if a is None:
                    continue
                if a.left is None and a.right is None:
                    out.append(a.val)
                stack.append(a.right)
                stack.append(a.left)
            return out
        return build(root1) == build(root2)

# Recursive method:
from typing import Optional, List
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Time: O(m^2 + n^2), m = number of nodes in root1, n = number of
        # nodes in root2
        # Space: O(h1 + h2) due to recursion stack, h1 = height of root1,
        # h2 = height of root2, worst case O(n + m) if both trees skewed
        def build(node: Optional[TreeNode]) -> List[int]:
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [node.val]
            return build(node.left) + build(node.right)
        return build(root1) == build(root2)


