# Time to write all of below including tests, explanation and time and aux
# and total space: 28 mins

# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import Optional, List
from collections import deque 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        nodes = []
        q = deque([(root, 1)])
        cur_level = 1
        while q:
            node, level = q.popleft()
            if node is None:
                continue
            if level > cur_level:
                out.append(nodes)
                nodes = []
                cur_level = level
            nodes.append(node.val)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
        if nodes:
            out.append(nodes)
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.levelOrder(None) == []
    assert sol.levelOrder(TreeNode(1)) == [[1]]
    assert sol.levelOrder(TreeNode(1, TreeNode(2))) == [[1], [2]]
    assert sol.levelOrder(TreeNode(0, TreeNode(-1), TreeNode(1))) == [[0], [-1, 1]]
    assert sol.levelOrder(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))) == [[1], [2, 3], [4]]

# Explanation: the code uses a breadth-first-search approach using a queue,
# and it stores the nodes' values at each level in the nodes list, and appends
# each level as a list to the out list
# Time: O(n), n = number of nodes in tree
# Space: excluding output: O(w), w = max number of nodes at any level


