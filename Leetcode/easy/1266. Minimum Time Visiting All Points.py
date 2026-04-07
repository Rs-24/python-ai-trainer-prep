# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/minimum-time-visiting-all-points/description/

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # Time: O(n), n = len(points)
        # Space: O(1)
        total = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            total += max(abs(x2 - x1), abs(y2 - y1))
        return total


