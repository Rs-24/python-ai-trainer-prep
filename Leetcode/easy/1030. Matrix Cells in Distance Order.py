# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/matrix-cells-in-distance-order/description/

from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # Time: O(n log n), n = rows * cols
        # Space: O(n)
        cells = []
        for r in range(rows):
            for c in range(cols):
                dist = abs(r - rCenter) + abs(c - cCenter)
                cells.append((dist, r, c))
        cells.sort()
        return [[r, c] for _, r, c in cells]


