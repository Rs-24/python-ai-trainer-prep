# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/weighted-word-mapping/description/

from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # Time: O(n), n = total number of characters in words
        # Space: O(n)
        def weight_to_letter(s: str) -> str:
            total = 0
            for ch in s:
                total += weights[ord(ch) - ord("a")]
            num = total % 26
            return chr(ord("a") + 25 - num)
        return "".join([weight_to_letter(word) for word in words])


