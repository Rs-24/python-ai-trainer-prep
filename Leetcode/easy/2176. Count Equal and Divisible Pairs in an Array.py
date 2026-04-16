# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/

from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Time: O(n^2), n = len(nums)
        # Space: O(n)
        count = 0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num1 == num2 and i * (i + j + 1) % k == 0:
                    count += 1
        return count


