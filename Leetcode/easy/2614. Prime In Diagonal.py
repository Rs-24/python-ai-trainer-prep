# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/prime-in-diagonal/description/

from typing import List
from math import sqrt

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        # Time: O(n * int(sqrt(k))), n = len(nums), k = average number found on
        # diagonals
        # Space: O(1)
        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            for d in range(2, int(sqrt(x)) + 1):
                if x % d == 0:
                    return False
            return True
        n = len(nums)
        best = 0
        for i in range(n):
            if is_prime(nums[i][i]):
                best = max(best, nums[i][i])
            if is_prime(nums[i][n - 1 - i]):
                best = max(best, nums[i][n - 1 - i])
        return best


