# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/

from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Space, excluding output: O(m + n)
        lucky = set()
        out = []
        for r in matrix:
            lucky.add(min(r))
        for c in range(len(matrix[0])):
            temp = []
            for r in range(len(matrix)):
                temp.append(matrix[r][c])
            if max(temp) in lucky:
                out.append(max(temp))
        return out

# Simpler version:
from typing import List
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(m * n), m = len(matrix), n = len(matrix[0])
        # Space: O(m + n)
        r = {min(r) for r in matrix}
        c = {max(c) for c in zip(*matrix)}
        return list(r & c)


