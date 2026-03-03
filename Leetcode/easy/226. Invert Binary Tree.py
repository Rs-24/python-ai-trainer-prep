# Time to write all of below including tests, explanation and time and aux
# and total space: 15 mins

# Problem: https://leetcode.com/problems/invert-binary-tree/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root

def inorder(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

if __name__ == "__main__":
    sol = Solution()
    assert sol.invertTree(None) == None
    assert inorder(sol.invertTree(TreeNode(1))) == [1]
    assert inorder(sol.invertTree(TreeNode(1, TreeNode(2), TreeNode(3)))) == [3, 1, 2]
    assert inorder(sol.invertTree(TreeNode(0, TreeNode(-1)))) == [0, -1]
    assert inorder(sol.invertTree(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)))) == [3, 1, 4, 2]

# Explanation: the code does a depth-first-search method using a stack, and
# inverts the children of each popped node
# Time: O(n), n = number of nodes in tree
# Space: excluding output: O(h), h = height of tree, worst case O(n) if tree
# skewed

# Iterative breadth-first-search method:
from collections import deque
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Time: O(n), n = number of nodes in tree
    # Space: excluding output: O(w), w = max width of tree
    q = deque([(root)])
    while q:
        node = q.popleft()
        if node is None:
            continue
        node.left, node.right = node.right, node.left
        q.append(node.left)
        q.append(node.right)
    return root

# Recursive method:
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Time: O(n), n = number of nodes in tree
    # Space: O(h) due to recursion stack, h = height of tree, worst case O(n)
    # if tree skewed
    if root is None:
        return root
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root


