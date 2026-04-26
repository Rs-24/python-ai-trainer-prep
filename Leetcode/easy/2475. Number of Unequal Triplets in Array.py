# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/number-of-unequal-triplets-in-array/description/

from typing import List
from collections import Counter

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        l = 0
        ans = 0
        n = len(nums)
        for f in c.values():
            r = n - l - f
            ans += l * f * r
            l += f
        return ans


