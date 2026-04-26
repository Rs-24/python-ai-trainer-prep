# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        inc = dec = 1
        best = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i - 1] > nums[i]:
                inc = 1
                dec += 1
            else:
                inc = dec = 1
            best = max(best, inc,  dec)
        return best


