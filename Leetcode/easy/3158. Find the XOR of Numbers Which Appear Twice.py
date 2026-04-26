# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/

from typing import List
from collections import Counter

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        total = 0
        for num, freq in c.items():
            if freq == 2:
                total ^= num
        return total


