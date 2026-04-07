# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/number-of-good-pairs/description/

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        d = {}
        total = 0
        for num in nums:
            if num in d:
                total += d[num]
                d[num] += 1
            else:
                d[num] = 1
        return total


