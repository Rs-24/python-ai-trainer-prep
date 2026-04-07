# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/unique-number-of-occurrences/description/

from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Time: O(n), n = len(arr)
        # Space: O(n)
        c = Counter(arr)
        freqs = [freq for _, freq in c.items()]
        return len(freqs) == len(set(freqs))


