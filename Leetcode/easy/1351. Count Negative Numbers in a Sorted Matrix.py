# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Time: O(m + n)
        # Space: O(1)
        m, n = len(grid), len(grid[0])
        total = 0
        r, c = m - 1, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                total += n - c
                r -= 1
            else:
                c += 1
        return total


