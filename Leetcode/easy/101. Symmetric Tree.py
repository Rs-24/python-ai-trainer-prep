# Time to write all of below including tests, why the solution works and time 
# and space complexity: 18 mins

# Problem: https://leetcode.com/problems/symmetric-tree/description/

from typing import Optional, Callable
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                continue
            if node.left is None and node.right is None:
                continue
            if node.left is None or node.right is None:
                return False
            if node.left.val != node.right.val:
                return False
            q.append(node.left)
            q.append(node.right)
        return True

def run_tests(f: Callable[[Optional[TreeNode]], bool]) -> None:
    tests = [(TreeNode(3), True), (TreeNode(0, TreeNode(-1)), False), (TreeNode(3, TreeNode(3), TreeNode(3)), True)]
    for root, expected in tests:
        actual = f(root)
        assert actual == expected, f"{f.__name__}({root}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    sol = Solution()
    run_tests(sol.isSymmetric)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - An iterative breadth-first-search method is used with a queue. While the 
#     queue is not empty, the leftmost node is popped and its children are checked
#     to see if they are symmetrical, and if so they are appended to the queue. 
#     Once the loop ends, True is returned
#
# Time: O(k), k = number of nodes whose children are checked, worst case O(n) if
# tree fully symmetrical, n = number of nodes in tree
# Aux space: O(w), w = widest level reached without non-symmetrical children, worst
# case O(n) if tree fully symmetrical
# 
# Learning lessons (done after completing all of above in 18 mins):
#   - I realise now that my solution is wrong in that it only checks if a node's 
#     children are equal and not if the whole tree is actually symmetrical, e.g.
#           1
#         /   \
#        2     2
#       / \   / \
#      3   4 4   3
#     is symmetrical but would return False because 3 != 4, hence I will rewrite
#     my algorithm and my rewrite is below:
#
# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#     # Time: O(k), k = number of nodes visited before mismatch, worst case O(n)
#     # if tree fully symmetrical
#     # Aux space: O(w), w = widest level reached without mismatch, worst case 
#     # O(n) if tree fully symmetrical 
#     if root is None:
#         return True
#     q = deque([(root.left, root.right)])
#     while q:
#         a, b = q.popleft()
#         if a is None and b is None:
#             continue
#         if a is None or b is None:
#             return False
#         if a.val != b.val:
#             return False       
#         q.append((a.left, b.right))
#         q.append((a.right, b.left))
#     return True
#
#   - Additionally, it would have been good to include a more difficult test to
#     illustrate how the original solution is flawed and how my rewrite is
#     correct, e.g. [1, 2, 2, null, 3, null, 3] -> False
#   - Additionally, another method would be to use a recursive mirror check, 
#     and my attempt is below:
# 
# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#     # Time: O(k), k = number of nodes compared before mismatch, worst case
#     # O(n) if tree fully symmetrical, n = number of nodes in tree
#     # Aux space: O(h) due to recursion stack, h = max depth reached before
#     # mismatch, worst case O(n) if trees fully symmetrical and skewed on both
#     # sides
#     if root is None:
#         return True
#     def check(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
#         if a is None and b is None:
#             return True
#         if a is None or b is None:
#             return False
#         return (a.val == b.val and
#                 check(a.left, b.right) and
#                 check(a.right, b.left))
#     return check(root.left, root.right)
#
#   - Additionally, another method would be to use an iterative depth-first-search
#     method. My attempt is below:
#
# from typing import List, Tuple
# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#     # Time: O(k), k = number of nodes compared before mismatch, worst case O(n)
#     # if tree fully symmetrical
#     # Aux space: O(h), h = length of deepest path explored without mismatch,
#     # worst case O(n) if tree fully symmetrical and skewed on both sides
#     if not root:
#         return True
#     stack: List[Tuple[Optional[TreeNode], Optional[TreeNode]]] = [(root.left, root.right)]
#     while stack:
#         a, b = stack.pop()
#         if not a and not b:
#             continue
#         if not a or not b:
#             return False
#         if a.val != b.val:
#             return False
#         stack.append((a.left, b.right))
#         stack.append((a.right, b.left))
#     return True



        









