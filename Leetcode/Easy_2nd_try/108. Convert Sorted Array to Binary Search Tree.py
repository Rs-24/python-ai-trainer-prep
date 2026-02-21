# Time to write all of below including tests, explanation and time and aux 
# space: 57 mins

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
        root = None
        stack = [(0, len(nums) - 1, None, None)]
        while stack:
            l, r, parent, side = stack.pop()
            if l > r:
                continue
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            if parent is None:
                root = node
            elif side == "L":
                parent.left = node
            elif side == "R":
                parent.right = node
            stack.append((l, mid - 1, node, "L"))
            stack.append((mid + 1, r, node, "R"))
        return root

def inorder(root: Optional[TreeNode]) -> list:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

from typing import Tuple
def height_and_balanced(root: Optional[TreeNode]) -> Tuple[int, bool]:
    if root is None:
        return 0, True
    lh, lb = height_and_balanced(root.left)
    rh, rb = height_and_balanced(root.right)
    balanced = lb and rb and abs(lh - rh) <= 1
    return 1 + max(lh, rh), balanced

def node_count(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + node_count(root.left) + node_count(root.right)

if __name__ == "__main__":
    sol = Solution()

    nums = [1]
    ans = sol.sortedArrayToBST(nums)
    assert inorder(ans) == nums
    assert height_and_balanced(ans)[1] == True
    assert node_count(ans) == len(nums)

    nums = [-1, 0, 1]
    ans = sol.sortedArrayToBST(nums)
    assert inorder(ans) == nums
    assert height_and_balanced(ans)[1] == True
    assert node_count(ans) == len(nums)

    nums = [1, 2, 3, 4, 5]
    ans = sol.sortedArrayToBST(nums)
    assert inorder(ans) == nums
    assert height_and_balanced(ans)[1] == True
    assert node_count(ans) == len(nums)

# Explanation: the code uses a depth-first-search approach using a stack by 
# starting with the mid value of the list and each sublist and builds the
# tree as it goes along
# Time (of sortedArrayToBST() only): O(n), n = len(nums)
# Space (of sortedArrayToBST() only): excluding output: worst case O(n)

# Learning lessons (done after completing all of above in 57 mins):
#   - It would be useful to know the iterative
#     breadth-first-search version, my attempt is below:
#
# from collections import deque
# def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#     # Time: O(n), n = len(nums)
#     # Space: excluding output: worst case O(n)
#     root = None
#     q = deque([(0, len(nums) - 1, None, None)]) 
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
#         elif side == "R":
#             parent.right = node
#         q.append((l, mid - 1, node, "L"))
#         q.append((mid + 1, r, node, "R"))
#     return root
#
#   - Additionally, it would be useful to know the recursive method, my
#     attempt is below:
#
# def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#     # Time: O(n), n = len(nums)
#     # Space: excluding output: O(log n) due to recursion stack
#     def build(l: int, r: int) -> Optional[TreeNode]:
#         if l > r:
#             return None
#         mid = (l + r) // 2
#         node = TreeNode(nums[mid])
#         node.left = build(l, mid - 1)
#         node.right = build(mid + 1, r)
#         return node
#     return build(0, len(nums) - 1)











