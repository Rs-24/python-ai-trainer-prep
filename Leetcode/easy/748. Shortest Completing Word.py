

from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Time: O(m + n), m = len(licensePlate), n = total number of
        # characters in words
        # Space: O(n + k), k = average number of letters per word in words
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        best_idx = -1
        for i, word in enumerate(words):
            have = Counter(word)
            if all(have[ch] >= need[ch] for ch in need):
                if best_idx == -1 or len(word) < len(words[best_idx]):
                    best_idx = i
        return words[best_idx]


