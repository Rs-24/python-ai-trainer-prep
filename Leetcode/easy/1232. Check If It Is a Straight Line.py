# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Time: O(n), n = len(coordinates)
        # Space: O(1)
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x1 - x0
        dy = y1 - y0
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x0) * dy != (y - y0) * dx:
                return False
        return True


