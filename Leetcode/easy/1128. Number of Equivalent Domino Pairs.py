# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/

from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Time: O(n), n = len(dominoes)
        # Space: O(n)
        d = {}
        total = 0
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            total += d.get(key, 0)
            d[key] = d.get(key, 0) + 1
        return total


