# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/description/

from typing import List
from collections import Counter

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        total = 0
        for num in nums:
            if c[num] % k == 0:
                total += num
        return total


