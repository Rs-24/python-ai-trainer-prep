# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/description/

from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # Time: O(m * n), m = len(grid), n = len(grid[0])
        # Aux space: O(1)
        out = []
        for c in range(len(grid[0])):
            best = 0
            for r in range(len(grid)):
                best = max(best, len(str(grid[r][c])))
            out.append(best)
        return out


