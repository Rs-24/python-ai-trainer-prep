# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/flip-square-submatrix-vertically/description/

from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # Time: O(k^2)
        # Space: O(1)
        r = x
        bottom = x + k - 1
        while r < bottom:
            for c in range(y, y + k):
                grid[r][c], grid[bottom][c] = grid[bottom][c], grid[r][c]
            r += 1
            bottom -= 1
        return grid


