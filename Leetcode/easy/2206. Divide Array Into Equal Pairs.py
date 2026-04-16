# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/divide-array-into-equal-pairs/description/

from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        c = Counter(nums)
        for num, freq in c.items():
            if freq % 2 != 0:
                return False
        return True


