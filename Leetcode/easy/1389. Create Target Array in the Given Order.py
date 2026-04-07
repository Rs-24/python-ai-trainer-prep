# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/create-target-array-in-the-given-order/description/

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # Time: O(n^2), n = len(nums) = len(index)
        # Space, excluding output: O(1)
        out = []
        for num, idx in zip(nums, index):
            out.insert(idx, num)
        return out


