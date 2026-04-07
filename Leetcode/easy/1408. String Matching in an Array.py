# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/string-matching-in-an-array/description/

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Time: O(n^2 * k), n = len(words), k = average string comparison cost
        # Space, excluding output: O(1)
        out = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    out.append(word)
                    break
        return out


