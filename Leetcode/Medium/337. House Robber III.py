

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(n)
        def dfs(n):
            if not n:
                return (0, 0)
            lr, ln = dfs(n.left)
            rr, rn = dfs(n.right)
            r = n.val + ln + rn
            nr = max(lr, ln) + max(rr, rn)
            return (r, nr)
        return max(dfs(root))
 

