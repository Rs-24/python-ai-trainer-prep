# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Time: O(m * n), m = len(mat), n = len(mat[0])
        # Space: O(m + n)
        m, n = len(mat), len(mat[0])
        special_r = [0] * m
        special_c = [0] * n
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    special_r[r] += 1
                    special_c[c] += 1
        total = 0
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    if special_r[r] == 1 and special_c[c] == 1:
                        total += 1
        return total


