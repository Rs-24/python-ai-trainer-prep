# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/

from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # Time: O(m * n), m = len(patterns), n = len(word)
        # Space: O(1)
        count = 0
        for p in patterns:
            if p in word:
                count += 1
        return count


