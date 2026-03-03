# Time to write all of below including tests, why the solution works and time 
# and space complexity: 15 mins

# Problem: https://leetcode.com/problems/same-tree/description/

from typing import Optional
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
        if not p or not q:
            return False
        p_q = deque([p])
        q_q = deque([q])
        while p_q and q_q:
            p1 = p_q.popleft()
            q1 = q_q.popleft()

            if not p1 and not q1:
                continue
            if not p1 or not q1:
                return False

            if p1.val != q1.val:
                return False
            
            p_q.append(p1.left)
            p_q.append(p1.right)

            q_q.append(q1.left)
            q_q.append(q1.right)
        
        return len(p_q) == len(q_q)

if __name__ == "__main__":
    sol = Solution()
    assert sol.isSameTree(None, None) == True
    assert sol.isSameTree(TreeNode(1), None) == False
    assert sol.isSameTree(None, TreeNode(1)) == False
    assert sol.isSameTree(TreeNode(1), TreeNode(1)) == True
    assert sol.isSameTree(TreeNode(1), TreeNode(1, None, TreeNode(2))) == False
    assert sol.isSameTree(TreeNode(-1, TreeNode(0), TreeNode(1)), TreeNode(-1, TreeNode(0), TreeNode(1))) == True
    assert sol.isSameTree(TreeNode(-1, TreeNode(0), TreeNode(1)), TreeNode(-1, TreeNode(-1), TreeNode(1))) == False

# Explanation: the code does a breadth-first-search of both trees using two
# queues to determine if they are structurally the same while also checking if
# the nodes have the same value
# Time: worst case O(n) if trees identical, n = number of nodes in either tree
# Aux space, excluding output and input: worst case O(w) if trees identical, 
# w = max number of nodes at any level in either tree (max width)
# Aux space, including output, excluding input: worst case O(w)

# Same solution but with queue of pairs
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Time: worst case O(n) if trees identical, n = number of nodes in either
    # tree
    # Aux space, excluding output and input: worst case O(w) if trees
    # identical, w = max number of nodes at any level in either tree (max width)
    # Total space, including output, excluding input: worst case O(w)
    if not p and not q:
        return True
    if not p or not q:
        return False
    pq = deque([(p, q)])
    while pq:
        a, b = pq.popleft()
        if not a and not b:
            continue
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        pq.append((a.left, b.left))
        pq.append((a.right, b.right))
    return True

# Recursive solution:
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Time: worst case O(n) if trees identical, n = number of nodes in either
    # tree
    # Aux space, excluding output and input: O(h) due to recursion stack,
    # h = max depth reached until mismatch or end reached if trees identical,
    # worst case O(n) if trees identical and skewed
    # Total space, including output, excluding input: O(h), worst case O(n)    
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Iterative depth-first-search solution using stack of pairs:
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Time: worst case O(n) if trees identical, n = number of nodes in either
    # tree
    # Aux space, excluding output and input: worst case O(h) if trees
    # identical, h = height of either tree, also worst case O(n) if trees
    # skewed 
    # Total space, including output, excluding input: worst case O(h), also
    # worst case O(n)
    stack = [(p, q)]
    while stack:
        a, b = stack.pop()
        if not a and not b:
            continue
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        stack.append((a.left, b.left))
        stack.append((a.right, b.right))
    return True


