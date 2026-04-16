# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/find-closest-number-to-zero/description/

from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        best = nums[0]
        for num in nums:
            if abs(num) < abs(best):
                best = num
            elif abs(num) == abs(best) and num > best:
                best = num
        return best


