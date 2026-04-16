# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        covered = [False] * 51
        for a, b in ranges:
            for i in range(a, b + 1):
                covered[i] = True
        for i in range(left, right + 1):
            if not covered[i]:
                return False
        return True


