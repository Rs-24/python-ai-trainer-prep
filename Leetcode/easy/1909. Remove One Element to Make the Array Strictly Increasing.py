# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/

from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        removed = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                removed += 1
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
        return removed <= 1


