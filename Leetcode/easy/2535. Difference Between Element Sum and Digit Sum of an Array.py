# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # Time: O(d), d = total number of digits in nums
        # Space: O(1)
        def sum_digits(x: int) -> int:
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total
        e_sum = sum(nums)
        d_sum = sum(sum_digits(num) for num in nums)
        return abs(e_sum - d_sum)


