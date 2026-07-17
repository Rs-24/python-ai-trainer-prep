

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: list) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        s = []
        for x in nums:
            t = TreeNode(x)
            while s and s[-1].val < x:
                t.left = s.pop()
            if s:
                s[-1].right = t
            s.append(t)
        return s[0]


