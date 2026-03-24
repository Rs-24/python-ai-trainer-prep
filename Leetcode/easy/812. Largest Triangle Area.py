# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/largest-triangle-area/description/

from typing import List 

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Time: O(n^3), n = len(points)
        # Space: O(1)
        best = 0.0
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                for k in range(j + 1, len(points)):
                    x3, y3 = points[k]
                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    best = max(best, area)
        return best


