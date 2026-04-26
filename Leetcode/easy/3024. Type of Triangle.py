# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/type-of-triangle/description/

from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Time: O(1)
        # Space: O(1)
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        s = set(nums)
        if len(s) == 1:
            return "equilateral"
        elif len(s) == 2:
            return "isosceles"
        return "scalene"


