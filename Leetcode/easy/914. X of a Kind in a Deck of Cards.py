# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/

from typing import List
from math import gcd
from collections import Counter
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # Time: O(n), n = len(deck)
        # Space: O(n)
        c = Counter(deck)
        d = reduce(gcd, c.values())
        return d >= 2


