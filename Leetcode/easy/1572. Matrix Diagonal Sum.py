# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/matrix-diagonal-sum/description/

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # Time: O(n), n = len(mat) = len(mat[0])
        # Space: O(1)
        total = 0
        n = len(mat)
        for i in range(n):
            total += (mat[i][i] + mat[i][n - 1 - i])
        if n % 2 != 0:
            total -= mat[n // 2][n // 2]
        return total


