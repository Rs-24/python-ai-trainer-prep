# Time to write all of below including tests, explanation and time and aux
# and total space: 28 mins

# Problem: https://leetcode.com/problems/validate-binary-search-tree/description/

from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode], low, high) -> bool:
            if node is None:
                return True            
            if low >= node.val or node.val >= high:
                return False
            return check(node.left, low, node.val) and check(node.right, node.val, high)
        return check(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    sol = Solution()
    assert sol.isValidBST(TreeNode(1)) == True
    assert sol.isValidBST(TreeNode(0, TreeNode(-1), TreeNode(1))) == True
    assert sol.isValidBST(TreeNode(1, TreeNode(2))) == False
    assert sol.isValidBST(TreeNode(1, TreeNode(1))) == False
    assert sol.isValidBST(TreeNode(0, TreeNode(-1, None, TreeNode(1)))) == False

# Explanation: the code uses recursion with high and low variables to
# determine if each node is valid
# Time: O(k), k = number of nodes processed, worst case O(n),
# n = number of nodes in tree
# Space: O(h) due to recursion stack, h = height of tree, worst case
# O(n) if tree skewed

# inorder traversal method:
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time: O(k), k = number of nodes processed, worst case O(n),
        # n = number of nodes in tree
        # Space: O(h), h = max height reached, worst case O(n) if tree skewed
        stack = []
        cur = root
        prev = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev and cur.val <= prev:
                return False
            prev = cur.val
            cur = cur.right
        return True


