# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/build-array-from-permutation/description/

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space, excluding output: O(1)
        out = []
        for i in range(len(nums)):
            out.append(nums[nums[i]])
        return out


