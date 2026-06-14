

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # Time: O(n)
        # Space: O(n)
        d = {}
        for i, ch in enumerate(s):
            d[ch] = i
        return sum(abs(d[ch] - i) for i, ch in enumerate(t))


