

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        def dfs(n: TreeNode):
            if not n:
                return 0, None
            ld, l_lca = dfs(n.left)
            rd, r_lca = dfs(n.right)
            if ld > rd:
                return ld + 1, l_lca
            if rd > ld:
                return rd + 1, r_lca
            return ld + 1, n
        return dfs(root)[1]


