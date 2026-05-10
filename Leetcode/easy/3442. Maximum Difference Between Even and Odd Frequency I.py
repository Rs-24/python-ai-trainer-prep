# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/

from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        c = Counter(s)
        max_odd = 0
        min_even = float("inf")
        for v in c.values():
            if v % 2 != 0:
                max_odd = max(max_odd, v)
            else:
                min_even = min(min_even, v)
        return max_odd - min_even


