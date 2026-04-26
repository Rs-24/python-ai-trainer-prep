# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/find-the-array-concatenation-value/description/

from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        # Time: O(d), total number of digits in nums
        # Space: O(1)
        def join(x1: int, x2: int) -> int:
            mul = 10
            while mul <= x2:
                mul *= 10
            return x1 * mul + x2
        total = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                total += nums[l]
                break
            total += join(nums[l], nums[r])
            l += 1
            r -= 1
        return total


