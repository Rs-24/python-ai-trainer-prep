# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/

from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # Time: O(n^2), n = len(nums)
        # Space: O(n)
        total = 0
        for i in range(len(nums)):
            seen = set()
            for j in range(i, len(nums)):
                seen.add(nums[j])
                total += len(seen) ** 2
        return total


