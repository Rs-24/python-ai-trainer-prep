

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        if not inorder:
            return None
        r = TreeNode(postorder[-1])
        s = [r]
        i = len(inorder) - 1
        for j in range(len(postorder) - 2, -1, -1):
            n = TreeNode(postorder[j])
            if s[-1].val != inorder[i]:
                s[-1].right = n
                s.append(n)
            else:
                t = None
                while s and s[-1].val == inorder[i]:
                    t = s.pop()
                    i -= 1
                t.left = n
                s.append(n)
        return r


