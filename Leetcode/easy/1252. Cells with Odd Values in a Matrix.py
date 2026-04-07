# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/

from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Time: O(m + n + len(indices))
        # Space: O(m + n)
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
        odd_rows = sum(rows)
        odd_cols = sum(cols)
        return odd_rows * (n - odd_cols) + odd_cols * (m - odd_rows)


