# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/

from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # Time: O(n log m), n = len(nums), m = max(nums)
        # Space: O(1) 
        def get_sum(x: int):
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total
        for i, num in enumerate(nums):
            if get_sum(num) == i:
                return i
        return -1


