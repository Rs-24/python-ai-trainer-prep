# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/monotonic-array/description/

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        increasing = None
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                if increasing is None:
                    increasing = nums[i - 1] < nums[i]
                elif (nums[i - 1] < nums[i]) != increasing:
                    return False
        return True


