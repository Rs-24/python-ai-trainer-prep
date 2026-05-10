# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/

from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        l_sum = 0
        r_sum = sum(nums)
        count = 0
        for i in range(len(nums) - 1):
            l_sum += nums[i]
            r_sum -= nums[i]
            if (l_sum - r_sum) % 2 == 0:
                count += 1
        return count


