# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-if-any-element-has-prime-frequency/description/

from typing import List
from math import sqrt
from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        # Time: O(n * sqrt(x)), n = len(nums), x = average frequency of
        # elements in nums
        # Space: O(n)
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True
        c = Counter(nums)
        for freq in c.values():
            if is_prime(freq):
                return True
        return False


