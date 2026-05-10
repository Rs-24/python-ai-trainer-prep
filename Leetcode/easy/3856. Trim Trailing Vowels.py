# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/trim-trailing-vowels/description/

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        i = len(s) - 1
        while i >= 0:
            if s[i] not in "aeiou":
                break
            i -= 1
        return s[:i + 1]


