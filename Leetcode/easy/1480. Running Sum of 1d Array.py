# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/running-sum-of-1d-array/description/

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space, excluding output: O(1)
        out = []
        total = 0
        for num in nums:
            total += num
            out.append(total)
        return out


