# Time to write all of below including tests, explanation and time and aux 
# space: 19 mins

# Problem: https://leetcode.com/problems/balanced-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, False)]
        height = {None: 0}
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                lh = height[node.left]
                rh = height[node.right]
                if abs(lh - rh) > 1:
                    return False
                height[node] = 1 + max(lh, rh)
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isBalanced(None) == True
    assert sol.isBalanced(TreeNode(1)) == True
    assert sol.isBalanced(TreeNode(1, TreeNode(2))) == True
    assert sol.isBalanced(TreeNode(-1, TreeNode(0), TreeNode(1))) == True
    assert sol.isBalanced(TreeNode(1, TreeNode(2, None, TreeNode(3)))) == False
    assert sol.isBalanced(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4))) == True

# Explanation: the code uses an iterative depth-first-search approach with a
# stack and checks the height of the left and right child of each node using
# a dictionary which stores the height of each node
# Time: O(k), k = number of nodes processed, worst case O(n),
# n = number of nodes in tree
# Space: O(k), worst case O(n)

# Recursive method:
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Time: O(k), k = number of nodes processed, worst case O(n),
        # n = number of nodes in tree
        # Space: O(h) due to recursion stack, h = max height reached, worst
        # case O(n) if tree skewed
        def height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            if lh == -1 or rh == -1 or abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)
        return height(root) != -1
        

