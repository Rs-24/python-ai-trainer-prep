# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        min1 = float("inf")
        min2 = float("inf")
        for num in nums[1:]:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num 
        return nums[0] + min1 + min2


