# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/maximum-average-subarray-i/description/

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        total = 0
        for i in range(k):
            total += nums[i]
        best = total
        for i in range(k, len(nums)):
            total -= nums[i - k]
            total += nums[i]
            best = max(best, total)
        return best / k


