# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Time: O(m + n), m = total number of characters in words, 
        # n = len(chars)
        # Space: O(1)
        count = [0] * 26
        for ch in chars:
            count[ord(ch) - ord("a")] += 1
        total = 0
        for word in words:
            temp = [0] * 26
            for ch in word:
                temp[ord(ch) - ord("a")] += 1
            if all(temp[i] <= count[i] for i in range(26)):
                total += len(word)
        return total


