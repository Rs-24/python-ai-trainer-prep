# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/

from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Time: O(m * n), m, n = len(mat), len(mat[0])
        # Space: O(m * n)
        m, n = len(mat), len(mat[0])
        def rotate(x: List[List[int]]) -> List[List[int]]:
            out = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    out[j][n - 1 - i] = x[i][j]
            return out
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False


