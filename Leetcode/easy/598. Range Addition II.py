# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/range-addition-ii/description/

from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Time: O(N), N = len(ops)
        # Space: O(1)
        if len(ops) == 0:
            return m * n        
        x_min = y_min = float("inf")
        for x, y in ops:
            x_min = min(x_min, x)
            y_min = min(y_min, y)
        return x_min * y_min


