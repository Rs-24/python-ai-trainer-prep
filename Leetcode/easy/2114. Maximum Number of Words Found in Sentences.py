# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/

from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Time: O(n), n = total number of characters in sentences
        # Space: O(n)
        return max(len(s.split()) for s in sentences)


