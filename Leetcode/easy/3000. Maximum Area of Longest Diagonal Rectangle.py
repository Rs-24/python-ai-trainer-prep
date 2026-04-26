# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/

from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # Time: O(n), n = len(dimensions)
        # Space: O(1)
        best = 0
        corresponding_area = 0
        for l, w in dimensions:
            d_squared = l**2 + w**2
            a = l * w
            if d_squared > best:
                best = d_squared
                corresponding_area = a
            elif d_squared == best:
                if a > corresponding_area:
                    best = d_squared
                    corresponding_area = a
        return corresponding_area


