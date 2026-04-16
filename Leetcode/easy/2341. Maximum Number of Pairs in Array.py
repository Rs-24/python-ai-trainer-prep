# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # Time: O(n), n = len(nums)
        # Aux space: O(n)
        c = Counter(nums)
        return [sum(freq // 2 for freq in c.values()), sum(freq % 2 for freq in c.values())]


