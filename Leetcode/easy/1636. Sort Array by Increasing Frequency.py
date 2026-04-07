# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/sort-array-by-increasing-frequency/description/

from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Time: O(n log n), n = len(nums)
        # Space, excluding output: O(n)
        c = Counter(nums)
        nums.sort(key=lambda x: (c[x], -x))
        return nums


