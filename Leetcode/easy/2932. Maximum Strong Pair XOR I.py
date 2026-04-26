# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-strong-pair-xor-i/description/

from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Time: O(n^2), n = len(nums)
        # Space: O(1)
        best = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    best = max(best, x ^ y)
        return best


