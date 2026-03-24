# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/detect-capital/description/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Time: O(n), n = len(word)
        # Space: O(n)
        capital = word[0].isupper()
        any_upper = False
        any_lower = False
        for ch in word[1:]:
            if ch.isupper():
                any_upper = True
                if any_lower or not capital:
                    return False
            if ch.islower():
                any_lower = True
                if any_upper:
                    return False
        return True

# One-liner method:
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Time: O(n), n = len(word)
        # Space: O(1)
        return word.isupper() or word.islower() or word.istitle()


