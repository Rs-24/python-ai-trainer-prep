

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: list) -> list:
        # Time: O(n)
        # Space: O(n)
        s = set(to_delete)
        a = []
        def dfs(n: TreeNode):
            if not n:
                return None
            n.left = dfs(n.left)
            n.right = dfs(n.right)
            if n.val not in s:
                return n
            if n.left:
                a.append(n.left)
            if n.right:
                a.append(n.right)
            return None
        if dfs(root):
            a.append(root)
        return a


