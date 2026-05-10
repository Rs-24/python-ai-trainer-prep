# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/

from typing import List
from collections import Counter

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        return [num for num, freq in c.items() if freq == 2]


