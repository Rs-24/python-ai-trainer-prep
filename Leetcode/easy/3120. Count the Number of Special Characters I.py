

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for i in range(26) if chr(ord("a") + i) in set(word) and chr(ord("a") + i).upper() in set(word))


