# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/largest-local-values-in-a-matrix/description/

from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # Time: O((n - 2)^2), n = len(grid) = len(grid[0])
        # Aux space: O(1)
        def max_val(r: int, c: int):
            best = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    best = max(best, grid[r + i][c + j])
            return best
        n = len(grid)
        out = [[0] * (n - 2) for _ in range(n - 2)]
        for r in range(1, n - 1):
            for c in range(1, n - 1):
                out[r - 1][c - 1] = max_val(r, c)
        return out
            

