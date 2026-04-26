# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/

from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(1)
        def count_set_bits(x: int):
            count = 0
            while x > 0:
                x &= (x - 1)
                count += 1
            return count
        return sum(num for i, num in enumerate(nums) if count_set_bits(i) == k)


