# Time to write all of below including tests, why the solution works and time 
# and space complexity: 24 mins

# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            out.append(node.val)
            node = node.right
        return out
   
if __name__ == "__main__":
    sol = Solution()
    assert sol.inorderTraversal(None) == []
    assert sol.inorderTraversal(TreeNode(1)) == [1]
    assert sol.inorderTraversal(TreeNode(-1, TreeNode(0), TreeNode(1))) == [0, -1, 1]
    assert sol.inorderTraversal(TreeNode(1, TreeNode(2, TreeNode(3)))) == [3, 2, 1]
    assert sol.inorderTraversal(TreeNode(1, None, TreeNode(2, None, TreeNode(3)))) == [1, 2, 3]
    
# Explanation: the code uses a depth-first-search approach using a stack to
# find the inorder traversal (left node -> current node -> right node) by
# first going as far down the left subtree of each node as possible
# Time: O(n), n = number of nodes in tree
# Aux space, excluding output and input: O(h), h = height of tree, worst case
# O(n) if tree only consists of one skewed left subtree
# Total space, including output, excluding input: O(n) 

# Recursive solution:
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # Time: O(n), n = number of nodes in tree
    # Aux space, excluding output and input: O(h), h = height of tree due to
    # recursion stack, worst case O(n) if tree skewed
    # Total space, including output, excluding input: O(n)    
    out = []
    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        out.append(node.val)
        dfs(node.right)
    dfs(root)
    return out


