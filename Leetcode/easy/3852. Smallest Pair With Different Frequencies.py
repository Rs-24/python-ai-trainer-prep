# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/smallest-pair-with-different-frequencies/description/

from typing import List
from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        # Time: O(n^2), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        unique = sorted(c.keys())
        best = None
        for i in range(len(unique)):
            for j in range(i + 1, len(unique)):
                x, y = unique[i], unique[j]
                if c[x] != c[y]:
                    if best is None or x < best[0] or (x == best[0] and y < best[1]):
                        best = [x, y]
        return best if best is not None else [-1, -1]


