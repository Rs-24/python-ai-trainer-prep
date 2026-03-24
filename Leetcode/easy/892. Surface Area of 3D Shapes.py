# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/surface-area-of-3d-shapes/description/

from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        # Time: O(m * n), m = len(grid), n = len(grid[0])
        # Space: O(1)
        base = sum(1 for row in grid for val in row if val > 0)
        side1 = sum(max(row) for row in grid)
        side2 = 0
        for c in range(len(grid[0])):
            tallest = 0
            for r in range(len(grid)):
                tallest = max(tallest, grid[r][c])
            side2 += tallest
        return 2 * (base + side1 + side2)


