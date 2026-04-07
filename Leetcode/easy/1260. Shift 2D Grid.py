# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/shift-2d-grid/description/

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(m * n), m = len(grid), n = len(grid[0])
        # Space, excluding output: O(1)
        rows, cols = len(grid), len(grid[0])
        out = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                new_pos = (r * cols + c + k) % (rows * cols)
                i, j = divmod(new_pos, cols)
                out[i][j] = grid[r][c]
        return out


