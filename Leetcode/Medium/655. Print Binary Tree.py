

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: TreeNode) -> list[list]:
        # Time: O(n)
        # Space: O(n)
        def height(n):
            if not n:
                return -1
            return 1 + max(height(n.left), height(n.right))
        h = height(root)
        r = h + 1
        c = (1 << (h + 1)) - 1
        o = [[""] * c for _ in range(r)]
        def dfs(n, r, c, t):
            if not n:
                return
            o[r][c] = str(n.val)
            if n.left:
                dfs(n.left, r + 1, c - t, t // 2)
            if n.right:
                dfs(n.right, r + 1, c + t, t // 2)
        dfs(root, 0, (c - 1) // 2, 1 << (h - 1))
        return o


        