# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/toeplitz-matrix/description/

from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Space: O(1)
        def check(r: int, c: int) -> bool:
            val = matrix[r][c]
            r += 1
            c += 1
            while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                if matrix[r][c] != val:
                    return False
                r += 1
                c += 1
            return True
        for i in range(len(matrix)):
            if not check(i, 0):
                return False
        for i in range(1, len(matrix[0])):
            if not check(0, i):
                return False
        return True

# Simpler version:
from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Space: O(1)
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
        return True


