# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Time: O(m + n), m, n = total number of characters in word1, word2,
        # respectively
        # Space: O(m + n)
        return "".join(word1) == "".join(word2)


