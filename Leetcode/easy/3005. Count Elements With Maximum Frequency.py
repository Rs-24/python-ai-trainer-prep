# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-elements-with-maximum-frequency/description/

from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        best = max(c.values())
        return sum(freq for num, freq in c.items() if freq == best)


