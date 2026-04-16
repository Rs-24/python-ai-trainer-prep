# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/sort-even-and-odd-indices-independently/description/

from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        nums[::2] = sorted(nums[::2])
        nums[1::2] = sorted(nums[1::2], reverse = True)
        return nums


