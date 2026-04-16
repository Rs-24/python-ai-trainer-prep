# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/count-special-quadruplets/description/

from typing import List
from collections import defaultdict

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # Time: O(n^2), n = len(nums)
        # Space: O(n^2)
        diff = defaultdict(int)
        count = 0
        for b in range(len(nums) - 3, 0, -1):
            c = b + 1
            for d in range(c + 1, len(nums)):
                diff[nums[d] - nums[c]] += 1
            for a in range(b):
                count += diff[nums[a] + nums[b]]
        return count


