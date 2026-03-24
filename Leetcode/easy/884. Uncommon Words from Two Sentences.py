# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Time: O(m + n), m = len(s1), n = len(s2)
        # Space, excluding output: O(k), k = number of unique words in s1 and
        # s2 combined
        c = Counter((s1 + " " + s2).split())
        return [word for word, freq in c.items() if freq == 1]


