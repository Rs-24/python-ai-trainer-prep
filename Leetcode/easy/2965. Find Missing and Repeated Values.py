# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-missing-and-repeated-values/description/

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Time: O(n^2), n = len(grid) = len(grid[0])
        # Space: O(n^2)
        n = len(grid)
        count = [0] * (n**2)
        for r in range(n):
            for c in range(n):
                count[grid[r][c] - 1] += 1
        repeated = -1
        missing = -1
        for i in range(n**2):
            if count[i] == 0:
                missing = i + 1
            elif count[i] == 2:
                repeated = i + 1
        return [repeated, missing] 


