# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-grid-satisfies-conditions/description/

from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        # Time: O(m * n), m = len(grid), n = len(grid[0])
        # Space: O(1)
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if r < m - 1 and grid[r][c] != grid[r + 1][c]:
                    return False
                if c < n - 1 and grid[r][c] == grid[r][c + 1]:
                    return False
        return True


