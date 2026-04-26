# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        return max(nums) * k + (k * (k - 1)) // 2


