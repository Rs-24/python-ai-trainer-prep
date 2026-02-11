# Time to write all of below including tests, explanation and time and aux
# and total space: 32 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        return

if __name__ == "__main__":
    sol = Solution()
    assert sol.kthSmallest(None, 1) == None
    assert sol.kthSmallest(None, 2) == None
    assert sol.kthSmallest(TreeNode(1), 1) == 1
    assert sol.kthSmallest(TreeNode(1, TreeNode(0), TreeNode(2)), 1) == 0
    assert sol.kthSmallest(TreeNode(1, TreeNode(0), TreeNode(2)), 2) == 1
    assert sol.kthSmallest(TreeNode(1, TreeNode(0), TreeNode(2)), 3) == 2
    assert sol.kthSmallest(TreeNode(1, None, TreeNode(2, None, TreeNode(3))), 1) == 1
    assert sol.kthSmallest(TreeNode(1, None, TreeNode(2, None, TreeNode(3))), 2) == 2
    assert sol.kthSmallest(TreeNode(1, None, TreeNode(2, None, TreeNode(3))), 3) == 3
    assert sol.kthSmallest(TreeNode(3, TreeNode(2, TreeNode(1))), 1) == 1
    assert sol.kthSmallest(TreeNode(3, TreeNode(2, TreeNode(1))), 2) == 2
    assert sol.kthSmallest(TreeNode(3, TreeNode(2, TreeNode(1))), 3) == 3

# Explanation: the code does an inorder traversal using a stack and
# consistently decrements k to find the k'th smallest element
# Time: worst case O(n), n = number of elements in tree
# Aux space, excluding output and input: O(h), h = height of tree
# Total space, including output, excluding input: O(h)

# Learning lessons (done after completing all of above in 32 mins):
#   - It would be useful to be able to explain how to optimise the code
#     if the BST is modified often, my attempt is below: 
#
# If the BST is modified often, then to optimise the algorithm I would 
# augment each node to store left_size, where left_size
# corresponds to the size of the left subtree. Then for each node, 
# if k <= left_size, then the k'th smallest element is in the left subtree,
# if k = left_size + 1, then it is the current node's value, and otherwise 
# it is in the right subtree. This would have a time complexity of O(h),
# where h = height of tree. If the tree is modified, e.g. with insertion
# and deletion operations, then left_size can be updated for the relevant
# nodes

