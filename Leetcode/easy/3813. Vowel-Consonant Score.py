

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for ch in s if ch in "aeiou") // sum(1 for ch in s if ch.isalpha() and ch not in "aeiou") if sum(1 for ch in s if ch.isalpha() and ch not in "aeiou") > 0 else 0


