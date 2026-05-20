

class Solution:
    def minTimeToType(self, word: str) -> int:
        # Time: O(n), n = len(word)
        # Space: O(1)
        total = 0
        prev = "a"
        for ch in word:
            diff = abs(ord(ch) - ord(prev))
            total += min(diff, 26 - diff)
            prev = ch
        return total + len(word)


