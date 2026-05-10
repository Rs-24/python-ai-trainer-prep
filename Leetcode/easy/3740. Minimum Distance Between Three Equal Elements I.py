# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/

from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        d = defaultdict(list)
        best = float("inf")
        for i, num in enumerate(nums):
            d[num].append(i)
            if len(d[num]) >= 3:
                a, b, c = d[num][-3], d[num][-2], d[num][-1]
                best = min(best, abs(a - b) + abs(b - c) + abs(a - c))
                d[num].pop(0)
        return best if best != float("inf") else -1


