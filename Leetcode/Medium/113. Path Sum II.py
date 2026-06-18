

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list]:
        # Time: O(n)
        # Space: O(n^2)
        out = []
        def dfs(n, r, p):
            if not n:
                return
            p.append(n.val)
            r -= n.val
            if not n.left and not n.right and r == 0:
                out.append(p[:])
            dfs(n.left, r, p)
            dfs(n.right, r, p)
            p.pop()
        dfs(root, targetSum, [])
        return out


