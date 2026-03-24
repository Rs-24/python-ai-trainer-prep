# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/rectangle-overlap/description/

from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Time: O(1)
        # Space: O(1)
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2
        return x1 < a2 and x2 > a1 and y1 < b2 and y2 > b1


