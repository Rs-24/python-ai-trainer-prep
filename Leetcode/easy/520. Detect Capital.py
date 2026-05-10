

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Time: O(n), n = len(word)
        # Space: O(1) 
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0].isupper() and all(word[i].islower() for i in range(1, len(word))):
            return True
        return False


