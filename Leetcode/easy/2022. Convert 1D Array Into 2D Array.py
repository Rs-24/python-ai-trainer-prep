# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Time: O(m * n)
        # Aux space: O(1)
        if m * n != len(original):
            return []
        out = [[0] * n for _ in range(m)]
        for i, num in enumerate(original):
            out[i // n][i % n] = num
        return out


