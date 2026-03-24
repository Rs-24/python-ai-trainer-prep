# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/projection-area-of-3d-shapes/description/

from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # Time: O(n^2), n = len(grid) = len(grid[0])
        # Space: O(1)
        xy = sum(1 for row in grid for val in row if val > 0)
        xz = sum(max(row) for row in grid)
        yz = 0
        for c in range(len(grid[0])):
            best = 0
            for r in range(len(grid)):
                best = max(best, grid[r][c])
            yz += best
        return xy + xz + yz


