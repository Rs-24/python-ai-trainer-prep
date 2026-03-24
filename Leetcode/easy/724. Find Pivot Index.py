# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/find-pivot-index/description/

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l_sum = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            r_sum = total - l_sum - num
            if l_sum == r_sum:
                return i
            l_sum += num
        return -1


