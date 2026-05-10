# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/

from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        c = Counter(s)
        vowels = set("aeiou")
        max_v = max_c = 0
        for ch, freq in c.items():
            if ch in vowels:
                max_v = max(max_v, freq)
            else:
                max_c = max(max_c, freq)
        return max_v + max_c


