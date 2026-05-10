# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/compute-alternating-sum/description/

from typing import List

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        sign = 1
        total = 0
        for num in nums:
            total += sign * num
            sign *= -1
        return total


