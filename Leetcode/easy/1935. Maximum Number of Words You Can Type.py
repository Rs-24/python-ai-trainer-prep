

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Time: O(m + n), m = len(text), n = len(brokenLetters)
        # Space: O(m)
        b = set(brokenLetters)
        return sum(all(ch not in b for ch in w) for w in text.split())


