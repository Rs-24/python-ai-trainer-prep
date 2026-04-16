# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Time: O(m + n), m = len(nums), n = min(nums)
        # Space: O(1)
        l, h = min(nums), max(nums)
        for x in range(min(l, h), 0, -1):
            if l % x == 0 and h % x == 0:
                return x


