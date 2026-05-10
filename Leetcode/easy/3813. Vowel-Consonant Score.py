# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/vowel-consonant-score/description/

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        vowels = set("aeiou")
        v = c = 0
        for ch in s:
            if ch.isalpha():
                if ch in vowels:
                    v += 1
                else:
                    c += 1
        return v // c if c > 0 else 0


