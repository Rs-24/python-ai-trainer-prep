

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Time: O(n^2)
        # Space: O(n)
        best = ""
        for i in range(len(s)):
            u = set()
            l = set()
            for j in range(i, len(s)):
                if s[j].isupper():
                    u.add(s[j])
                else:
                    l.add(s[j])
                if u == {ch.upper() for ch in l} and l == {ch.lower() for ch in u}:
                    if j - i + 1 > len(best):
                        best = s[i:j + 1]
        return best


