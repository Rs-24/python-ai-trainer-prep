# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/longest-alternating-subarray/description/

from typing import List

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        best = -1
        cur = 1
        expected_diff = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff == expected_diff:
                cur += 1
                expected_diff *= -1
            elif diff == 1:
                cur = 2
                expected_diff = -1
            else:
                cur = 1
                expected_diff = 1
            if cur >= 2:
                best = max(best, cur)
        return best


