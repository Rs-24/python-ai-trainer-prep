
from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # Time: O(n), n = total number of characters in words
        # Space: O(n)
        c = Counter(words[0])
        for i in range(1, len(words)):
            c &= Counter(words[i])
        out = []
        for ch, freq in c.items():
            out.extend([ch] * freq)
        return out
   

