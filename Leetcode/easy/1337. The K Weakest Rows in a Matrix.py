# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Time: O(m * n + m log m), m = len(mat), n = len(mat[0])
        # Space: O(m)
        rows = []
        for i in range(len(mat)):
            rows.append((sum(mat[i]), i))
        rows.sort()
        return [i for _, i in rows[:k]]
        

