# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/

from typing import List
from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Time: O(k), k = total characters in words
        # Space: O(1)
        c = Counter()
        for word in words:
            c.update(word)
        n = len(words)
        for freq in c.values():
            if freq % n != 0:
                return False
        return True


