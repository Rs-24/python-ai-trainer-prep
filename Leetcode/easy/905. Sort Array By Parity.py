# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/sort-array-by-parity/description/

from typing import List 

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 0:
                l += 1
            while l < r and nums[r] % 2 != 0:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums


