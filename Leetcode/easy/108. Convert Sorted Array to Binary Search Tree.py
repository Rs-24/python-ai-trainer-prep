# Time to write all of below including tests, explanation and time and aux 
# space: 43 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return []
        elif len(nums) == 1:
            return TreeNode(nums[0])
        
        if len(nums) % 2 == 0:
            mid = (len(nums) / 2) - 1
        else:
            mid = len(nums) // 2

        root = TreeNode(nums[mid])

        i = mid - 1
        node = root
        while i >= 0:
            node.left = TreeNode(nums[i])
            if i == 0:
                break
            node = node.left
            i -= 1

        i = mid + 1
        node = root
        while i < len(nums):
            node.right = TreeNode(nums[i])
            if i == len(nums) - 1:
                break
            node = node.right
            i += 1
        
        return root
    
# Tests: 
# [1] -> [1]
# [-1, 0, 1] -> [0, -1, 1]
# [1, 3] -> [1, null, 3]

# Explanation: The root is set to the middle number, and the remaining numbers
# in nums are added as nodes in each corresponding side
# Time: O(n), n = len(nums)
# Aux space: O(1)

# Learning lessons (done after completing all of above in 43 mins):
#   - I now realise my solution is flawed as it doesn't produce a proper 
#     height balanced BST as the tree will be skewed on both sides, making it
#     inefficient. Hence, my recursive rewrite is below:
#
# def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#     # Time: O(n), n = len(nums)
#     # Aux space: O(log n) due to recursion stack
#     def build(l: int, r: int) -> Optional[TreeNode]:
#         if l > r:
#             return None
#         mid = (l + r) // 2
#         node = TreeNode(nums[mid])
#         node.left = build(l, mid-1)
#         node.right = build(mid+1, r)
#         return node
#     return build(0, len(nums)-1)
#
# Additionally, it would be useful to know the iterative stack version, my
# attempt is below:
#
# def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#     # Time: O(n), n = len(nums)
#     # Aux space: O(log n), worst case O(n)
#     if not nums:
#         return None
#     root = None
#     stack = [(0, len(nums)-1, None, None)]
#     while stack:
#         l, r, parent, side = stack.pop()
#         if l > r:
#             continue
#         mid = (l + r) // 2
#         node = TreeNode(nums[mid])
#         if parent is None:
#             root = node
#         elif side == "L":
#             parent.left = node
#         elif side == "R":
#             parent.right = node
#         stack.append((l, mid-1, node, "L"))
#         stack.append((mid+1, r, node, "R"))
#     return root
#
# Additionally, it would be useful to know the iterative breadth-first-search
# version, my attempt is below:
#
# from collections import deque
# def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#     # Time: O(n), n = len(nums)
#     # Aux space: O(n)
#     if not nums:
#         return None
#     root = None
#     q = deque([(0, len(nums)-1, None, None)])
#     while q:
#         l, r, parent, side = q.popleft()
#         if l > r:
#             continue
#         mid = (l + r) // 2
#         node = TreeNode(nums[mid])
#         if parent is None:
#             root = node
#         elif side == "L":
#             parent.left = node
#         else:
#             parent.right = node
#         q.append((l, mid-1, node, "L"))
#         q.append((mid+1, r, node, "R"))
#     return root
#
# Additionally, I could have improved my testing structure a bit. My rewrite
# is below:
#
# Tests: 
# edge cases: 
#   [1]
#   [-1, 0, 1, 2]
#   [1, 2] 
# Property tests:
#   - inorder(tree) == nums
#   - For every node, abs(height(left) - height(right)) <= 1
#   - node_count(tree) == len(nums)












