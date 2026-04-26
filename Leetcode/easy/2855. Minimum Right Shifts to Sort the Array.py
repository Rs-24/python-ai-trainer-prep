# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/description/

from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        break_point = -1
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if break_point != -1:
                    return -1
                break_point = i
        if break_point == -1:
            return 0
        if nums[0] < nums[-1]:
            return -1
        return len(nums) - break_point


