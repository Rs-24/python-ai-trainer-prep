

class Solution:
    def isAcronym(self, words: list, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        if len(words) != len(s):
            return False
        return all(w[0] == ch for w, ch in zip(words, s))


