# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/description/

from typing import List

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        ans = 0
        for num in nums:
            if num % 2 == 0:
                ans |= num
        return ans


