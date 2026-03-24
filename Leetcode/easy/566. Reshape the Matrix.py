# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/reshape-the-matrix/description/

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Time: O(m * n), m = len(mat), n = len(mat[0])
        # Space, excluding output: O(1)
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        out = [[0] * c for _ in range(r)]
        for i in range(m * n):
            out[i // c][i % c] = mat[i // n][i % n]
        return out


