

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # Time: O(n)
        # Space: O(n)
        q = deque([root])
        t = False
        while q:
            n = q.popleft()
            if n is None:
                t = True
            else:
                if t:
                    return False
                q.append(n.left)
                q.append(n.right)
        return True


        