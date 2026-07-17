

from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> list:
        # Time: O(n)
        # Space: O(n)
        if not root:
            return []
        d = defaultdict(int)
        def dfs(n) -> int:
            if not n:
                return 0
            t = n.val + dfs(n.left) + dfs(n.right)
            d[t] += 1
            return t
        dfs(root)
        t = max(d.values())
        return [x for x, f in d.items() if f == t]


