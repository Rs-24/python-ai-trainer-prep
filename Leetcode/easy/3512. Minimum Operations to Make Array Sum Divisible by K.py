# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        return sum(nums) % k


