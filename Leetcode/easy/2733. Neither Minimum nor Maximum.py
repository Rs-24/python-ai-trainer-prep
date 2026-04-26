# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/neither-minimum-nor-maximum/description/

from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l, h = min(nums), max(nums)
        for num in nums:
            if num != l and num != h:
                return num
        return -1


