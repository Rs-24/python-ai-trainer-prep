

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        s = s.split()
        return " ".join(s[:k])


