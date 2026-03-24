# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/array-partition/description/

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: worst case O(n)
        nums.sort()
        return sum(nums[::2])


