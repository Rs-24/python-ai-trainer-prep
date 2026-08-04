

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: list) -> list:
        # Time: O(n)
        # Space: O(n)
        i = 0
        a = []
        def dfs(n) -> bool:
            nonlocal i
            if not n:
                return True
            if n.val != voyage[i]:
                return False
            i += 1
            if n.left and i < len(voyage) and n.left.val != voyage[i]:
                a.append(n.val)
                return dfs(n.right) and dfs(n.left)
            return dfs(n.left) and dfs(n.right)
        return a if dfs(root) else [-1]


        