# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        best = float("inf")
        nums.sort()
        for i in range(len(nums) - k + 1):
            best = min(best, nums[i + k - 1] - nums[i])
        return best


