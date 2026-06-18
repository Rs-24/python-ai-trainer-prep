

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        # Time: O(n)
        # Space: O(n)
        if not preorder:
            return None
        r = TreeNode(preorder[0])
        s = [r]
        i = 0
        for j in range(1, len(preorder)):
            n = TreeNode(preorder[j])
            if s[-1].val != inorder[i]:
                s[-1].left = n
                s.append(n)
            else:
                t = None
                while s and s[-1].val == inorder[i]:
                    t = s.pop()
                    i += 1
                t.right = n
                s.append(n)
        return r


