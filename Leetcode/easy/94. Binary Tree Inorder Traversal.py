# 204

from typing import List, Optional, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path: List[Any] = [root]
        output: List[int] = []
        cur = root
        while True:
            while cur.left:
                cur = cur.left
                path.append(cur)
                       
            output.append(cur.val)
            
            if cur.right:
                cur = cur.right
                path.append(cur)
            else:
                path.pop()
                cur = path[-1]

            # if cur.left.val != "null":
            #     path.append(cur)
            #     cur = cur.left
            # else:
            #     if cur.val != "null":
            #         output.append(cur.val)
            #         path.append(cur)
            #         cur = cur.right
            #     else:
            #         if cur.right.val != "null":
            #             path.append(cur)
            #             cur = cur.right
            #         else:
            #             cur.val 
            #             cur = path.pop()






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def inorderTraversal(self, root: Optional['TreeNode']) -> List[int]:
        result = []
        stack = []
        current = root

        # Inorder = Left -> Node -> Right
        while current or stack:
            # 1) Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # 2) Visit the node on top of the stack
            current = stack.pop()
            result.append(current.val)

            # 3) Then go to its right subtree
            current = current.right

        return result






