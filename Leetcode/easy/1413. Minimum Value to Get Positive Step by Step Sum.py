# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/

from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        cur = 0
        lowest = 0
        for num in nums:
            cur += num
            lowest = min(lowest, cur)
        return 1 - lowest


