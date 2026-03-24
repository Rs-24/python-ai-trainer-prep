# Time to write all of below including tests, explanation and time and aux
# and total space: 18 mins

# Problem: https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(n), n = number of nodes in tree
        # Space, excluding output: O(h) due to recursion stack, h = height of
        # tree, worst case O(n) if tree skewed
        prev = None
        out = []
        count = 0
        max_count = 0
        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal prev, out, count, max_count
            if not node:
                return None
            inorder(node.left)
            if node.val == prev:
                count += 1
            else:
                count = 1
            if count > max_count:
                max_count = count
                out = [node.val]
            elif count == max_count:
                out.append(node.val)
            prev = node.val
            inorder(node.right)
        inorder(root)
        return out

# Iterative depth-first-search method:
from typing import Optional, List
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(n), n = number of nodes in tree
        # Space, excluding output: O(h), h = height of tree, worst case O(n)
        # if tree skewed
        out = []
        stack = []
        cur = root
        prev = None
        count = 0
        max_count = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val == prev:
                count += 1
            else:
                count = 1
            if count == max_count:
                out.append(cur.val)
            elif count > max_count:
                max_count = count
                out = [cur.val]
            prev = cur.val
            cur = cur.right
        return out

# Recursive depth-first-search hash map method:
from typing import Optional, List
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Time: O(n), n = number of nodes in tree
        # Space, excluding output: worst case O(n)
        freqs = {}
        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return None
            inorder(node.left)
            freqs[node.val] = freqs.get(node.val, 0) + 1
            inorder(node.right)
        inorder(root)
        max_count = max(freqs.values())
        return [val for val, freq in freqs.items() if freq == max_count]

        # Space, excluding output: O(h) due to recursion stack, h = height of
        # tree, worst case O(n) if tree skewed

