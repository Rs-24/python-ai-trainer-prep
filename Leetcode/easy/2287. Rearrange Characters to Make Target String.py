

from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # Time: O(n)
        # Space: O(n)
        c1 = Counter(s)
        c2 = Counter(target)
        return min(c1[ch] // freq for ch, freq in c2.items())


