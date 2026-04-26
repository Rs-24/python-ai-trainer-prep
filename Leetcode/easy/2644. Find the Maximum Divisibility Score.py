# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-maximum-divisibility-score/description/

from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # Time: O(m * n), m = len(nums), n = len(divisors)
        # Space: O(1)
        best_divisor = float("inf")
        best_count = -1
        for i in range(len(divisors)):
            count = 0
            for j in range(len(nums)):
                if nums[j] % divisors[i] == 0:
                    count += 1
            if count > best_count or (count == best_count and divisors[i] < best_divisor):
                best_divisor = divisors[i]
                best_count = count
        return best_divisor


