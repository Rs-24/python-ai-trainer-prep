# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/description/

from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        # Time: O(n), n = len(forts)
        # Space: O(1)
        prev = [None, None]
        best = 0
        for i, ch in enumerate(forts):
            if abs(ch) == 1:
                if prev[0] is not None and prev[0] * ch == -1:
                    best = max(best, i - prev[1] - 1)
                prev = [ch, i]
        return best


