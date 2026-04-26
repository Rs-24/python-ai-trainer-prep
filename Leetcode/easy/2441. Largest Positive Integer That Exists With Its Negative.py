# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        seen = set(nums)
        best = -1
        for num in nums:
            if num > 0 and -num in seen:
                best = max(best, num)
        return best


