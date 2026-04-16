# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/maximum-ascending-subarray-sum/description/

from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        best = nums[0]
        cur = nums[0]
        for i, num in enumerate(nums[:-1]):
            if num < nums[i + 1]:
                cur += nums[i + 1]
            else:
                cur = nums[i + 1]
            best = max(best, cur)
        return best


