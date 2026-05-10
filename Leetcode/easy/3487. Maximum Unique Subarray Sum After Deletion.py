# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/

from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        mx = max(nums)
        if mx <= 0:
            return mx
        seen = set()
        ans = 0
        for num in nums:
            if num > 0 and num not in seen:
                ans += num
                seen.add(num)
        return ans


