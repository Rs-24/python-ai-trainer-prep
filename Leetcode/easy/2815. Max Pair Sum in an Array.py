# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/max-pair-sum-in-an-array/description/

from typing import List
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Time: O(d), d = total number of digits in nums
        # Space: O(d)
        def max_digit(x: int) -> int:
            return int(max(ch for ch in str(x)))
        def get_sum_of_max_two(arr: List[int]) -> int:
            if len(arr) < 2:
                return -1
            first = None
            second = None
            for num in arr:
                if first is None:
                    first = num
                elif num >= first:
                    second = first
                    first = num
                elif second is None or num > second:
                    second = num
            return first + second
        d = defaultdict(list)
        for num in nums:
            d[max_digit(num)].append(num)
        best = -1
        for _, a in d.items():
            if len(a) >= 2:
                best = max(best, get_sum_of_max_two(a))
        return best


