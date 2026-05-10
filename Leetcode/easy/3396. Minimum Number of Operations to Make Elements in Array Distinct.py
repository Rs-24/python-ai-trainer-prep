# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0


