# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/sum-of-variable-length-subarrays/description/

from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        res = 0
        for i, num in enumerate(nums):
            start = max(0, i - num)
            res += prefix[i + 1] - prefix[start]
        return res


