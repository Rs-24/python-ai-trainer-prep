# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/odd-string-difference/description/

from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:
        # Time: O(m * n), m = len(words)
        # Space: O(n)
        def convert(s: str) -> List[int]:
            out = []
            for i in range(len(s) - 1):
                out.append(ord(s[i + 1]) - ord(s[i]))
            return out
        c1 = convert(words[0])
        c2 = convert(words[1])
        c3 = convert(words[2])
        common = c1 if c1 == c2 or c1 == c3 else c2
        for word in words:
            if convert(word) != common:
                return word


