# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        nums.sort()
        n = len(nums)
        for i in range(1, n + 1):
            idx = n - i
            if nums[idx] >= i and (idx == 0 or nums[idx - 1] < i):
                return i
        return -1


