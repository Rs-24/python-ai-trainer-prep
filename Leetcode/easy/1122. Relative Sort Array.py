# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/relative-sort-array/description/

from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Time: O(n + k log k), n = len(arr1), k = number of leftover items in
        # arr1
        # Space, excluding output: O(n)
        out = []
        c = Counter(arr1)
        for num in arr2:
            out.extend([num] * c[num])
            del c[num]
        for num in sorted(c):
            out.extend([num] * c[num])
        return out


