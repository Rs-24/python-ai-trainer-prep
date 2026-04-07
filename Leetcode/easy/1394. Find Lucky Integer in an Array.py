# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/find-lucky-integer-in-an-array/description/

from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Time: O(n log n), n = len(arr)
        # Space: O(n)
        c = Counter(arr)
        for num in sorted(c.keys(), reverse=True):
            if c[num] == num:
                return num
        return -1


