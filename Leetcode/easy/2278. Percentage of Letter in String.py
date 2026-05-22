

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        # Time: O(n)
        # Space: O(1)
        return (100 * s.count(letter)) // len(s)


