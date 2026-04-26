# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-champion-i/description/

from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # Time: O(n^2), n = len(grid)
        # Space: O(1)
        n = len(grid)
        for c in range(n):
            champion = True
            for r in range(n):
                if r == c:
                    continue
                if grid[r][c] == 1:
                    champion = False
                    break
            if champion:
                return c


