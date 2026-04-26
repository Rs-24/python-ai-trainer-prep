# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/number-of-distinct-averages/description/

from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        nums.sort()
        avgs = set()
        l, r = 0, len(nums) - 1
        while l < r:
            avgs.add((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return len(avgs)


