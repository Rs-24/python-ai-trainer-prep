# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/

from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


