# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/number-of-beautiful-pairs/description/

from typing import List
from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        # Time: O(n^2), n = len(nums)
        # Space: O(1)
        def first_digit(x: int) -> int:
            while x >= 10:
                x //= 10
            return x
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if gcd(first_digit(nums[i]), nums[j] % 10) == 1:
                    count += 1
        return count


