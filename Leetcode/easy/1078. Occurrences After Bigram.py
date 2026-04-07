# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/occurrences-after-bigram/description/

from typing import List

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # Time: O(n), n = len(text)
        # Space, excluding output: O(n)
        out = []
        text = text.split()
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                out.append(text[i + 2])
        return out


