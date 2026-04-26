# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-operations-to-collect-elements/description/

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        seen = set()
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if 1 <= nums[i] <= k:
                seen.add(nums[i])
            count += 1
            if len(seen) == k:
                return count
        return len(nums)


