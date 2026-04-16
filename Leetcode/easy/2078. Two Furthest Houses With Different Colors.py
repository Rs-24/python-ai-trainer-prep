# Time to write all of below including tests, explanation and time and aux
# and total space: 2 min

# Problem: https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/

from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # Time: O(n), n = len(colors)
        # Space: O(1)
        best = 0
        n = len(colors)
        for i, c in enumerate(colors):
            if c != colors[0]:
                best = max(best, i)
            if c != colors[-1]:
                best = max(best, n - 1 - i)
        return best


