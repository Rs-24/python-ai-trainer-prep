# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/sum-of-squares-of-special-elements/description/

from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        total = 0
        for i, num in enumerate(nums):
            if n % (i + 1) == 0:
                total += num**2
        return total


