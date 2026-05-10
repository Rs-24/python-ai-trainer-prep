# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/maximum-subarray-with-equal-products/description/

from typing import List
from math import gcd

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # Time: O(n^2), n = len(nums)
        # Space: O(1)
        n = len(nums)
        best = 0
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)
                if prod == g * l:
                    best = max(best, j - i + 1)
        return best


