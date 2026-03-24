# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/sort-array-by-parity-ii/description/

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        even = 0
        odd = 1
        while even < n and odd < n:
            while even < n and nums[even] % 2 == 0:
                even += 2
            while odd < n and nums[odd] % 2 == 1:
                odd += 2
            if even < n and odd < n:
                nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2
        return nums


