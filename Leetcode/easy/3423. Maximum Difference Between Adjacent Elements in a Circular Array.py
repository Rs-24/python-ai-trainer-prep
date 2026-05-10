# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/

from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        best = 0
        prev = nums[-1]
        for num in nums:
            best = max(best, abs(num - prev))
            prev = num
        return best


