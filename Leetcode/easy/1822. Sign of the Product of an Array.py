# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign *= -1
        return sign


