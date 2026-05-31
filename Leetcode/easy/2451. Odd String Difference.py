

class Solution:
    def oddString(self, words: list) -> str:
        # Time: O(n)
        # Space: O(n)
        def convert(s: str) -> list:
            out = []
            for i in range(1, len(s)):
                out.append(ord(s[i]) - ord(s[i - 1]))
            return out
        c1 = convert(words[0])
        c2 = convert(words[1])
        c3 = convert(words[2])
        common = c1 if c1 == c2 or c1 == c3 else c2
        for word in words:
            if convert(word) != common:
                return word


