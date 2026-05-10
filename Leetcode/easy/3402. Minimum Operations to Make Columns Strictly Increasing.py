# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/description/

from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        # Time: O(m * n), m = len(grid), n = len(grid[0])
        # Space: O(1)
        count = 0
        for c in range(len(grid[0])):
            prev = grid[0][c]
            for r in range(1, len(grid)):
                if grid[r][c] <= prev:
                    diff = prev - grid[r][c] + 1
                    grid[r][c] += diff
                    count += diff
                prev = grid[r][c]
        return count


