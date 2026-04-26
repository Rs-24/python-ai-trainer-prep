# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/

from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # Time: O(m * n), m = len(mat), n = len(mat[0])
        # Space: O(n)
        m, n = len(mat), len(mat[0])
        k %= n
        for r in range(m):
            if r % 2 == 0:
                shifted = mat[r][k:] + mat[r][:k]
            else:
                shifted = mat[r][-k:] + mat[r][:-k]
            if shifted != mat[r]:
                return False
        return True


