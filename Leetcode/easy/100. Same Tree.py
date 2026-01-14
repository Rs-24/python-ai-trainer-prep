# Time to write all of below including tests, why the solution works and time 
# and space complexity: 28 mins

# Problem: https://leetcode.com/problems/same-tree/description/

from typing import Optional, Callable
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (p and not q) or (q and not p):
            return False

        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            cur1 = q1.popleft()
            cur2 = q2.popleft()
            if cur1.val != cur2.val:
                return False
            if cur1.left:
                q1.append(cur1.left)
            if cur1.right:
                q1.append(cur1.right)
            if cur2.left:
                q2.append(cur2.left)
            if cur2.right:
                q2.append(cur2.right)
        if len(q1) != len(q2):
            return False
        else:
            return True 

def run_tests(f: Callable[[Optional[TreeNode], Optional[TreeNode]], bool]) -> None:
    tests = [(TreeNode(-1,TreeNode(0),TreeNode(1)), TreeNode(-1,TreeNode(0),TreeNode(1)), True), (None, None, True), (TreeNode(1), TreeNode(1, TreeNode(2)), False)]
    for p, q, expected in tests:
        actual = f(p, q)
        assert actual == expected, f"{f.__name__}({p}, {q}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_tests(Solution.isSameTree)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - isSamTree() compares p and q, if they are both None then True is returned,
#     if only 1 is None, then False is returned. Then a breadth-first-search method
#     is used with two queues, and if at any point the popped value from each queue
#     is different to each other, then False is returned. Once either or both queues
#     become empty, then their lengths are compared. If they are the same, then True
#     is returned, otherwise False is returned   
#
# Time complexity: O(n + m), where n is the number of nodes in the tree with root p,
#                  and m is the number of nodes in the tree with root q
# Auxiliary space complexity: O(w1 + w2), where the w1 and w2 are the max number of 
#                             nodes in each tree at any level (max width). Worst
#                             case O(n + m)
#
#
# Learning lessons (done after completing all of above in 28 mins):
#   - There is a bug in that e.g. [1, None, 2], [1, 2, None] would return True
#     because the function doesn't compare whether both nodes in the current
#     iteration have left/right children. As such, I should add the checks:
#     if (cur1.left is None) != (cur2.left is None) : return False
#     if (cur1.right is None) != (cur2.right is None) : return False
#   - run_tests(Solution.isSameTree) wouldn't work, I would need to instead do e.g.
#     sol = Solution()
#     run_tests(sol.isSameTree)
#   - Additionally, it would be a good idea to know the recursive solution. My
#     attempt at it is below:
#
# def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#     # Time: O(k), k = number of nodes compared, worst case O(n) if identical,
#     # n = number of nodes in p and q
#     # Aux space: O(h), where h = height of longest explored path due to
#     # recursion stack, worst case O(n) if both are skewed and identical
#     if not p and not q:
#         return True
#     if not p or not q:
#         return False
#     return (p.val == q.val and 
#             self.isSameTree(p.left, q.left) and 
#             self.isSameTree(p.right, q.right))
#
#   - Additionally, the method in my solution was an iterative
#     breadth-first-search, however it could be improved by using a queue of
#     pairs. As such, my rewrite is below:
#
# def isSameTree_iter_bfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#     # Time: O(k), k = number of nodes compared, worst case O(n) if trees
#     # identical - in this case n = number of nodes in either tree  
#     # Aux space: O(w), w = width of widest level reached without mismatch, 
#     # worst case O(n) if trees identical
#     dq = deque([(p, q)])
#     while dq:
#         a, b = dq.popleft()
#         if a is None and b is None:
#             continue
#         if a is None or b is None:
#             return False
#         if a.val != b.val:
#             return False
#         dq.append((a.left, b.left))
#         dq.append((a.right, b.right))
#     return True
#
#   - Additionally, it may be useful to learn the iterative depth-first-search
#     using a stack of pairs. My attempt is below:
#
# from typing import List, Tuple
# def isSameTree_iter_dfs(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#     stack: List[Tuple[Optional[TreeNode], Optional[TreeNode]]] = [(p, q)]
#     while stack:
#         a, b = stack.pop()
#         if a is None and b is None:
#             continue
#         if a is None or b is None:
#             return False
#         if a.val != b.val:
#             return False
#         stack.append((a.left, b.left))
#         stack.append((a.right, b.right))
#     return True



