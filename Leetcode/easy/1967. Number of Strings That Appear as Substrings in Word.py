

class Solution:
    def numOfStrings(self, patterns: list, word: str) -> int:
        # Time O(n), n = total number of characters in patterns
        # Space: O(1)
        return sum(p in word for p in patterns)


