

class Solution:
    def prefixCount(self, words: list, pref: str) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for word in words if word.startswith(pref))


