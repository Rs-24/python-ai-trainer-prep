# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-operations-to-equalize-array/description/

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        return 0 if all(num == nums[0] for num in nums) else 1


