# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/left-and-right-sum-differences/description/

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Aux space: O(1)
        l_sum = 0
        r_sum = sum(nums)
        out = []
        for num in nums:
            r_sum -= num
            out.append(abs(l_sum - r_sum))
            l_sum += num
        return out


