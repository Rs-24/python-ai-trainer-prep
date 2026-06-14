

class Solution:
    def isValid(self, word: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        if len(word) < 3:
            return False
        if any(not ch.lower().isalpha() for ch in word):
            return False
        if not any(ch.lower() in "aeiou" for ch in word):
            return False
        if not any(ch.lower() not in "aeiou" for ch in word):
            return False
        return True


