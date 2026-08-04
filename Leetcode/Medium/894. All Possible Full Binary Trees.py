

from functools import lru_cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> list:
        # Time: O(n^2)
        # Space: O(n)
        @lru_cache(None)
        def b(x: int):
            if x % 2 == 0:
                return []
            if x == 1:
                return [TreeNode(0)]
            a = []
            for ln in range(1, x, 2):
                for l in b(ln):
                    for r in b(x - 1 - ln):
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        a.append(root)
            return a
        return b(n)


        