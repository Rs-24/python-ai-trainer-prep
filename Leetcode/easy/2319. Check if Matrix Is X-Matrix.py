# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/

from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        # Time: O(n^2), n = len(grid)
        # Space: O(1)
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if (r == c or r == n - 1 - c):
                    if grid[r][c] == 0:
                        return False
                else:
                    if grid[r][c] != 0:
                        return False
        return True


