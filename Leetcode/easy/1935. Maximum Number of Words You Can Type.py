# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Time: O(n), n = len(text)
        # Space: O(1)
        count = 0
        b = set(brokenLetters)
        for word in text.split():
            valid = True
            for ch in word:
                if ch in b:
                    valid = False
            count += 1 if valid else 0
        return count


