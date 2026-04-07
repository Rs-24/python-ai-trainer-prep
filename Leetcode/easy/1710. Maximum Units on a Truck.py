# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/maximum-units-on-a-truck/description/

from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Time: O(n log n), n = len(boxtypes)
        # Space: O(n)
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        total = 0
        for a, b in boxTypes:
            total += min(a, truckSize) * b
            truckSize -= min(a, truckSize)
        return total


