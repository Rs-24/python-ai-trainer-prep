# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-degree-of-each-vertex/description/

from typing import List

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Space: O(m)
        ans = [0] * len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[i] += matrix[i][j]
        return ans


