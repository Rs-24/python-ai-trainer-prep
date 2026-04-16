# Time to write all of below including tests, explanation and time and aux
# and total space: 2 min

# Problem: https://leetcode.com/problems/count-common-words-with-one-occurrence/description/

from typing import List
from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # Time: O(m + n), m = len(words1), n = len(words2)
        # Space: O(m + n)
        c1 = Counter(words1)
        c2 = Counter(words2)
        return sum(1 for word, freq in c1.items() if freq == 1 and c2[word] == 1)


