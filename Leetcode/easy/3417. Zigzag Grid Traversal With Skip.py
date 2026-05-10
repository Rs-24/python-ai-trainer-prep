# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/zigzag-grid-traversal-with-skip/description/

from typing import List

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        # Time: O(m * n), m = len(grid), n = len(grid)
        # Space: O(m * n)
        path = []
        reverse = False
        take = True
        for row in grid:
            if reverse:
               row.reverse()
            for x in row:
                if take:
                    path.append(x)
                take = not take
            reverse = not reverse
        return path


