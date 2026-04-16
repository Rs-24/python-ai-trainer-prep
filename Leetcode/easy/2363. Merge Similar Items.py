# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/merge-similar-items/description/

from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # Time: O(m + n + k log k), m = len(items1), n = len(items2), k = len(d)
        # Aux space: O(k)
        d = {}
        for a, b in items1:
            d[a] = d.get(a, 0) + b
        for a, b in items2:
            d[a] = d.get(a, 0) + b
        return [[num, d[num]] for num in sorted(d)]


