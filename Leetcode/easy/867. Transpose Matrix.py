# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/transpose-matrix/description/

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Space, excluding output: O(1)
        out = [[0] * len(matrix) for _ in range(len(matrix[0]))]        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                out[c][r] = matrix[r][c]
        return out


