

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        seen = set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)


