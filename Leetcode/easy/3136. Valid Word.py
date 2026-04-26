# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/valid-word/description/

class Solution:
    def isValid(self, word: str) -> bool:
        # Time: O(n), n = len(word)
        # Space: O(1)
        if len(word) < 3:
            return False
        vowel = False
        consonant = False
        for ch in word:
            if ch.isalpha():
                if ch.lower() in "aeiou":
                    vowel = True
                else:
                    consonant = True
            elif not ch.isdigit():
                return False
        return vowel and consonant


