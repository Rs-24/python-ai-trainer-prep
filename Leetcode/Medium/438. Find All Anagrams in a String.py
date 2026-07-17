

class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        # Time: O(n)
        # Space: O(n)
        if len(p) > len(s):
            return []
        t = [0] * 26
        for ch in p:
            t[ord(ch) - ord("a")] += 1
        w = [0] * 26
        for i in range(len(p)):
            w[ord(s[i]) - ord("a")] += 1
        o = []
        if t == w:
            o.append(0)
        for i in range(len(p), len(s)):
            w[ord(s[i]) - ord("a")] += 1
            w[ord(s[i - len(p)]) - ord("a")] -= 1
            if w == t:
                o.append(i - len(p) + 1)
        return o


