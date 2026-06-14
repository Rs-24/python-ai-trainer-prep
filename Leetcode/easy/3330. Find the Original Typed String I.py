

class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Time: O(n)
        # Space: O(1)
        return 1 + sum(word[i - 1] == word[i] for i in range(1, len(word)))


