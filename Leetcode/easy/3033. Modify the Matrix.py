# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/modify-the-matrix/description/

from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Aux space: O(m)
        m, n = len(matrix), len(matrix[0])
        answer = [[0] * n for _ in range(m)]
        max_cols = []
        for c in range(n):
            best = float("-inf")
            for r in range(m):
                answer[r][c] = matrix[r][c]
                best = max(best, matrix[r][c])
            max_cols.append(best)
        for r in range(m):
            for c in range(n):
                if answer[r][c] == -1:
                    answer[r][c] = max_cols[c]
        return answer


