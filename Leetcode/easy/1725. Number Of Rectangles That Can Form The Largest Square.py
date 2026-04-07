# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/description/

from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # Time: O(n), n = len(rectangles)
        # Space: O(1)
        best = 0
        count = 0
        for a, b in rectangles:
            side_length = min(a, b)
            if side_length > best:
                best = side_length
                count = 1
            elif side_length == best:
                count += 1
        return count


