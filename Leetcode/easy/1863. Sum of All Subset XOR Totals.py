# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Time: O(2^n), n = len(nums)
        # Space: O(n)
        def dfs(idx: int, xor_so_far: int):
            if idx == len(nums):
                return xor_so_far
            cur = xor_so_far ^ nums[idx]
            inc = dfs(idx + 1, cur)
            exc = dfs(idx + 1, xor_so_far)
            return inc + exc
        return dfs(0, 0)


