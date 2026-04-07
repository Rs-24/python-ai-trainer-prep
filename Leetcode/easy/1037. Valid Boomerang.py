# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/valid-boomerang/description/

from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Time: O(1)
        # Space: O(1)
        (x1, y1), (x2, y2), (x3, y3) = points
        return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)


