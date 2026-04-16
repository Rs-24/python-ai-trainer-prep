# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        c = Counter(s)
        return len(set(c.values())) == 1


