# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-positive-sum-subarray/description/

from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # Time: O(n^2), n = len(nums)
        # Space: O(1)
        n = len(nums)
        best = float("inf")
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                length = j - i + 1
                if length > r:
                    break
                if l <= length <= r and total > 0:
                    best = min(best, total)
        return -1 if best == float("inf") else best


