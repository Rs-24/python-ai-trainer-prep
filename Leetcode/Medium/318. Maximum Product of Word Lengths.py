

class Solution:
    def maxProduct(self, words: list) -> int:
        # Time: O(n^2 + n)
        # Space: O(n)
        n = len(words)
        m = [0] * n        
        for i, w in enumerate(words):
            t = 0
            for ch in w:
                t |= 1 << (ord(ch) - ord("a"))
            m[i] = t
        a = 0
        for i in range(n):
            for j in range(i + 1, n):
                if m[i] & m[j] == 0:
                    a = max(a, len(words[i]) * len(words[j]))
        return a


