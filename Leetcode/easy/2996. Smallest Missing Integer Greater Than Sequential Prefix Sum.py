# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        i = 0
        total = nums[0]
        while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
            total += nums[i + 1]
            i += 1
        s = set(nums)
        while total in s:
            total += 1
        return total


