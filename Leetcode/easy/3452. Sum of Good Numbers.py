# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/sum-of-good-numbers/description/

from typing import List

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        total = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if 0 <= i - k < n:
                if nums[i - k] >= num:
                    continue
            if 0 <= i + k < n:
                if nums[i + k] >= num:
                    continue
            total += num
        return total


