# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/split-the-array/description/

from typing import List
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        for freq in c.values():
            if freq > 2:
                return False
        return True


