# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/

from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Time: O(n log n), n = len(points)
        # Space: O(n)
        x = [a for a, _ in points]
        x.sort()
        best = 0
        for i in range(1, len(x)):
            best = max(best, x[i] - x[i - 1])
        return best


