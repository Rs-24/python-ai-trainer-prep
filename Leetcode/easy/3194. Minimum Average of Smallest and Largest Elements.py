# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/

from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # Time: O(n log n), n = len(nums)
        # Space: O(1)
        nums.sort()
        best = float("inf")
        l, r = 0, len(nums) - 1
        while l < r:
            best = min(best, (nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return best


