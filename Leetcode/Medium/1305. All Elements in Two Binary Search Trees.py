

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list:
        # Time: O(n)
        # Space: O(n)
        def inorder(n: TreeNode, arr: list) -> None:
            if not n:
                return
            inorder(n.left, arr)
            arr.append(n.val)
            inorder(n.right, arr)
        arr1, arr2 = [], []
        inorder(root1, arr1)
        inorder(root2, arr2)
        ans = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
        ans.extend(arr1[i:])
        ans.extend(arr2[j:])
        return ans


