# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/minimum-distance-to-the-target-element/description/

from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        best = float("inf")
        for i, num in enumerate(nums):
            if num == target:
                best = min(best, abs(i - start))
        return best


