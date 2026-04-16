# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/smallest-index-with-equal-value/description/

from typing import List

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        for i, num in enumerate(nums):
            if i % 10 == num:
                return i
        return -1


