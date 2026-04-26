# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-words-containing-character/description/

from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Time: O(n * m), n = len(words), m = average number of characters
        # per word
        # Space: O(n)
        return [i for i, word in enumerate(words) if x in word]


