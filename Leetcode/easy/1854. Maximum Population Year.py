# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/maximum-population-year/description/

from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Time: O(n), n = len(logs)
        # Space: O(1)
        years = [0] * 101
        for a, b in logs:
            for i in range(a, b):
                years[i - 1950] += 1
        best = max(years)
        for i, population in enumerate(years):
            if population == best:
                return i + 1950


