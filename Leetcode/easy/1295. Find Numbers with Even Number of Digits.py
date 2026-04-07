# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Time: O(n), n = total number of digits in nums
        # Space: O(1)
        total = 0
        for num in nums:
            digits = 0
            while num > 0:
                digits += 1
                num //= 10
            total += 1 if digits % 2 == 0 else 0
        return total


