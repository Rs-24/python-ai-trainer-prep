

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        # Time: O(n^2)
        # Space: O(n)
        self.a = None
        def dfs(n: TreeNode, t: list) -> None:
            if not n:
                return
            t.append(chr(n.val + ord("a")))
            if not n.left and not n.right:
                if self.a is None or "".join(reversed(t)) < self.a:
                    self.a = "".join(reversed(t))
            dfs(n.left, t)
            dfs(n.right, t)
            t.pop()
        dfs(root, [])
        return self.a


