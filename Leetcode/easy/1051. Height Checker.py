# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/height-checker/description/

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Time: O(n log n), n = len(heights)
        # Space: O(n)
        expected = sorted(heights)
        total = 0
        for i, height in enumerate(heights):
            if height != expected[i]:
                total += 1
        return total

# One-liner version:
from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Time: O(n log n)
        # Space: O(n)
        return sum(h != e for h, e in zip(heights, sorted(heights)))


