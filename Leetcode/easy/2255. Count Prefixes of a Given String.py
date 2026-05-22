

class Solution:
    def countPrefixes(self, words: list, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for word in words if s.startswith(word))


