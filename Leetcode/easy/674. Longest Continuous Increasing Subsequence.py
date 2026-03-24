# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l = 0
        best = 0
        prev = None
        for r, num in enumerate(nums):
            if prev is not None and prev >= num:
                l = r
            best = max(best, r - l + 1)
            prev = num
        return best


