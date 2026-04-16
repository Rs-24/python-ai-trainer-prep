# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/

from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # Time: O(n^2), n = len(matrix) = len(matrix[0])
        # Space: O(n)
        n = len(matrix) 
        for row in matrix:
            if len(set(row)) != n:
                return False
        for c in range(n):
            vals = set()
            for r in range(n):
                vals.add(matrix[r][c])
            if len(set(vals)) != n:
                return False
        return True


