# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Time: O(m + n), m = len(allowed), n = total number of characters in
        # words
        # Space: O(m)
        a = set(allowed)
        total = 0
        for word in words:
            valid = True
            for ch in word:
                if ch not in a:
                    valid = False
            total += 1 if valid else 0
        return total


