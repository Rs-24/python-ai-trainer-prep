

class Solution:
    def stringMatching(self, words: list) -> list:
        # Time: O(n^2), n = total number of characters in words
        # Space: O(n)
        out = []
        for w1 in words:
            for w2 in words:
                if w1 != w2 and w1 in w2:
                    out.append(w1)
                    break
        return out


