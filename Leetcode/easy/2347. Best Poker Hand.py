# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/best-poker-hand/description/

from typing import List
from collections import Counter

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # Time: O(m + n), m = len(ranks), n = len(suits)
        # Space: O(m + n)
        if len(set(suits)) == 1:
            return "Flush"
        c = Counter(ranks)
        best = max(c.values())
        if best >= 3:
            return "Three of a Kind"
        elif best == 2:
            return "Pair"
        return "High Card"


