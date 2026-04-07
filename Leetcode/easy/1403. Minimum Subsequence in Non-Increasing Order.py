# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/

from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # Time: O(n log n), n = len(nums)
        # Space, excluding output: O(n)
        nums.sort(reverse=True)
        total = sum(nums)
        cur = 0
        out = []
        for num in nums:
            out.append(num)
            cur += num
            if cur > total - cur:
                return out
            

