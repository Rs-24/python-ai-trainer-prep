# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/smallest-range-i/description/

from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        return max(0, max(nums) - min(nums) - 2 * k)


