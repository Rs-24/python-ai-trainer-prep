# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/

from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # Time: O(m + n), m = len(s), n = len(target)
        # Space: O(1)
        c1 = Counter(s)
        c2 = Counter(target)
        return min(c1[ch] // freq for ch, freq in c2.items())


