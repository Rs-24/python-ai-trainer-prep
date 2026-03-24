# Time to write all of below including tests, explanation and time and aux
# and total space: 13 mins

# Problem: https://leetcode.com/problems/shortest-completing-word/description/

from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Time: O(m + n), m = len(licensePlate), n = total number of
        # characters in words
        # Space, excluding output: O(1)
        need = [0] * 26
        for ch in licensePlate:
            if ch.isalpha():
                need[ord(ch.lower()) - ord("a")] += 1
        def is_valid(word: str) -> bool:
            have = [0] * 26
            for ch in word:
                have[ord(ch) - ord("a")] += 1
            for i in range(26):
                if have[i] < need[i]:
                    return False
            return True
        ans = ""
        for w in words:
            if is_valid(w):
                if ans == "" or len(w) < len(ans):
                    ans = w
        return ans

# Alternative method using Counter
from typing import List
from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Time: O(m + n), m = len(licensePlate), n = total number of
        # characters in words
        # Space, excluding output: O(1)
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        ans = ""
        for word in words:
            have = Counter(word)
            if all(have[ch] >= need[ch] for ch in need):
                if ans == "" or len(word) < len(ans):
                    ans = word
        return ans


