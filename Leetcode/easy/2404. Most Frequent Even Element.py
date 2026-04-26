# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/most-frequent-even-element/description/

from typing import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        e = Counter(num for num in nums if num % 2 == 0)
        if not e:
            return -1
        best_freq = max(e.values())
        smallest = max(e.keys())
        for num, freq in e.items():
            if freq == best_freq and num < smallest:
                smallest = num
        return smallest


