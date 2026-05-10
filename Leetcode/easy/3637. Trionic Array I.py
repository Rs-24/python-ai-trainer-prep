# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/trionic-array-i/description/

from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        if n < 4:
            return False
        i = 0
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        temp = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == temp or i == n - 1:
            return False
        temp = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == temp:
            return False
        return i == n - 1


