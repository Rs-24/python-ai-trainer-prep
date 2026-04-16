# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        min_so_far = nums[0]
        best = -1
        for num in nums[1:]:
            if num > min_so_far:
                best = max(best, num - min_so_far)
            elif num < min_so_far:
                min_so_far = num
        return best


