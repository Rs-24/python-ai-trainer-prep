# Time to write all of below including tests, why the solution works and time 
# and space complexity: 4h 14 mins

# I couldn't figure this one out for some reason, and I required help from
# chatGPT to solve it

# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

from typing import List, Optional, Any, Callable
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
        stack: List[Any] = []
        output: List[int] = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            output.append(cur.val)
            
            cur = cur.right
        return output
    
    @staticmethod
    def split_into_nodes(nums: List[Any]) -> TreeNode:
        if not nums or nums[0] == "null":
            return None
        root = TreeNode(nums[0])
        q = deque([root])
        i = 1
        while i < len(nums):
            cur = q.popleft()

            if nums[i] != "null":
                cur.left = TreeNode(nums[i])
                q.append(cur.left)
            i += 1

            if i >= len(nums):
                break

            if nums[i] != "null":
                cur.right = TreeNode(nums[i])
                q.append(cur.right)
            i += 1

        return root

def run_tests(f: Callable[[Optional[TreeNode]], List[int]]) -> None:
    tests = [([1, "null", 2, 3], [1, 3, 2]), ([], []), ([1], [1]), ([-1, 0, 1], [0, -1, 1])]
    for root, expected in tests:
        actual = f(Solution.split_into_nodes(root))
        assert actual == expected, f"{f.__name__}({root}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_tests(Solution.inorderTraversal)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - The TreeNode class is created, and within the Solution class there is the
#     solution function itself, inorderTraversal(), and split_into_nodes(). 
#     inorderTraversal() uses a stack to iterate through the nodes, and outputs 
#     the corresponding python list. split_into_nodes() takes in a python list
#     and iterates through it while building a binary tree of nodes, and returns
#     the root of the tree
#
# Time complexity (of inorderTraversal() only): O(n), where n = number of nodes in tree
# Auxiliary Space complexity (of inorderTraversal() only): O(n), where n = number of nodes in tree






