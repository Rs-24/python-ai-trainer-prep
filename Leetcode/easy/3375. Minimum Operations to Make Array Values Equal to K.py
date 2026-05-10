# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        seen = set()
        for num in nums:
            if num < k:
                return -1
            if num > k:
                seen.add(num)
        return len(seen)


