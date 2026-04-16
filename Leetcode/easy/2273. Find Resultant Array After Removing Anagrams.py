# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/

from typing import List
from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # Time: O(n), n = total number of characters in words
        # Aux space: O(1)
        out = []
        prev_counter = None
        for word in words:
            c = Counter(word)
            if c != prev_counter:
                out.append(word)
                prev_counter = c
        return out


