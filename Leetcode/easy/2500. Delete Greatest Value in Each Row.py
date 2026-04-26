# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # Time: O(m * n log n), m = len(grid), n = len(grid[0])
        # Space: O(n)
        for row in grid:
            row.sort()
        ans = 0
        for c in range(len(grid[0]) - 1, -1, -1):
            ans += max(grid[r][c] for r in range(len(grid)))
        return ans


