# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/make-array-elements-equal-to-zero/description/

from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l_sum = 0
        r_sum = sum(nums)
        res = 0
        for num in nums:
            r_sum -= num
            if num == 0:
                if l_sum == r_sum:
                    res += 2
                elif abs(l_sum - r_sum) == 1:
                    res += 1
            else:
                l_sum += num
        return res


