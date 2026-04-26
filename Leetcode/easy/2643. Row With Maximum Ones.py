# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/row-with-maximum-ones/description/

from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        # Time: O(m * n), m = len(mat), n = len(mat[0])
        # Space: O(1)
        out = [0, sum(mat[0])]
        for i, row in enumerate(mat):
            if sum(row) > out[1]:
                out = [i, sum(row)]
        return out


