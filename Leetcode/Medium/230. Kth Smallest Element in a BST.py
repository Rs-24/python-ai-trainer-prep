# Time to write all of below including tests, explanation and time and aux
# and total space: 32 mins

# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

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
# Time: O(h + k), k = number of nodes processed, h = height of tree,
# worst case O(n), n = number of nodes in tree
# Space: O(h), worst case O(n) if tree skewed


