# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/find-the-middle-index-in-array/description/

from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        r = sum(nums)
        l = 0
        for i, num in enumerate(nums):
            r -= num
            if l == r:
                return i
            l += num
        return -1


