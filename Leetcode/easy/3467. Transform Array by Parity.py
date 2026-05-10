# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/transform-array-by-parity/description/

from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        even = odd = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        return [0] * even + [1] * odd


