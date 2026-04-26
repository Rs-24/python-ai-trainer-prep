# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/description/

from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        return sum(num % 2 == 0 for num in nums) >= 2


