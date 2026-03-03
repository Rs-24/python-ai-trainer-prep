# Time to write all of below including tests, explanation and time and aux 
# space: 10 mins

# Problem: https://leetcode.com/problems/binary-tree-postorder-traversal/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                out.append(node.val)
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.postorderTraversal(None) == []
    assert sol.postorderTraversal(TreeNode(1)) == [1]
    assert sol.postorderTraversal(TreeNode(1, TreeNode(-1), TreeNode(0))) == [-1, 0, 1]
    
# Explanation: The function iterates over the tree using a depth-first-search
# approach using a stack of (node, visited) pairs, and once the stack 
# is empty returns the variable 'out'
# Time: O(n), n = number of nodes in tree
# Space: excluding output: O(h), h = height of tree, worst case O(n)
# if tree skewed

# Iterative method using prev pointer instead of visited flag:
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(n), n = number of nodes in tree
        # Space: excluding output: O(h), h = height of tree, worst case O(n)
        # if tree skewed
        out = []
        stack = []
        prev = None
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack[-1]
            if node.right and node.right != prev:
                cur = node.right
            else:
                out.append(node.val)
                prev = node
                stack.pop()
        return out

# Recursive depth-first-search method:
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # Time: O(n), n = number of nodes in tree
    # Space: excluding output: O(h) due to recursion stack, h = height of
    # tree, worst case O(n) if tree skewed
    out = []
    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return None
        dfs(node.left)
        dfs(node.right)
        out.append(node.val)
    dfs(root)
    return out


