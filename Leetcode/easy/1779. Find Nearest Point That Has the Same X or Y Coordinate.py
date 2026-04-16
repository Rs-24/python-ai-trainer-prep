# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/

from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # Time: O(n), n = len(points)
        # Space: O(1)
        ans = -1
        best = float("inf")
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                m_h = abs(a - x) + abs(b - y)
                if m_h < best:
                    best = m_h
                    ans = i
        return ans


