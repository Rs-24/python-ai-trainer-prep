

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # Time: O(n)
        # Space: O(n)
        l = r = 0
        def f(t: TreeNode) -> int:
            nonlocal l, r
            if not t:
                return 0
            a, b = f(t.left), f(t.right)
            if t.val == x:
                l, r = a, b
            return a + b + 1
        f(root)
        return max(l, r, n - l - r - 1) > n // 2


