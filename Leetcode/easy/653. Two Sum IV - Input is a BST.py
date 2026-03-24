# Time to write all of below including tests, explanation and time and aux
# and total space: 10 mins

# Problem: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Time: O(n), n = number of nodes in tree
        # Space: O(n)
        nums = []
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return None
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total == k:
                return True
            elif total > k:
                r -= 1
            else:
                l += 1
        return False

# Hash set method:
from typing import Optional
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Time: O(n), n = number of nodes in tree
        # Space: O(n)
        seen = set()
        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)


