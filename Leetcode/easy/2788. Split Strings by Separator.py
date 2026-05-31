

class Solution:
    def splitWordsBySeparator(self, words: list, separator: str) -> list:
        # Time: O(n)
        # Space: O(n)
        out = []
        for w in words:
            for p in w.split(separator):
                if p:
                    out.append(p)
        return out


