# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        res = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                diff = nums[i - 1] - nums[i] + 1
                nums[i] += diff
                res += diff
        return res


