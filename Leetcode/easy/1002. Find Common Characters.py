# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/find-common-characters/description/

from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Time: O(n), n = total number of characters in words
        # Space, excluding output: O(1)
        c = Counter(words[0])
        for word in words[1:]:
            c &= Counter(word)
        out = []
        for ch, freq in c.items():
            out.extend([ch] * freq)
        return out
    
# 26-length frequency array method:
from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Time: O(n), n = total number of characters in words
        # Space, excluding output: O(1)
        min_freqs = [float("inf")] * 26
        for word in words:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            for i in range(26):
                min_freqs[i] = min(min_freqs[i], count[i])
        out = []
        for i in range(26):
            out.extend([chr(i + ord("a"))] * min_freqs[i])
        return out
       

