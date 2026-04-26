# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/apple-redistribution-into-boxes/description/

from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Time: O(m + n log n), m = len(apple), n = len(capacity)
        # Space: O(m)
        total = sum(apple)
        capacity.sort(reverse=True)
        cur = 0
        for i, c in enumerate(capacity):
            cur += c
            if cur >= total:
                return i + 1


