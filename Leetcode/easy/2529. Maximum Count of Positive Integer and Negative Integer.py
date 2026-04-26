# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Time: O(log n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < 0:
                l = mid + 1
            else:
                r = mid
        negatives = l
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid
        positives = n - l
        return max(negatives, positives)


