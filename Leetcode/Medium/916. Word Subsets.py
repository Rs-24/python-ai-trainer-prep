

class Solution:
    def wordSubsets(self, words1: list, words2: list) -> list:
        # Time: O(n)
        # Space: O(n)
        c = [0] * 26
        for w in words2:
            t = [0] * 26
            for ch in w:
                t[ord(ch) - ord("a")] += 1
            for i in range(26):
                c[i] = max(c[i], t[i])
        a = []
        for w in words1:
            t = [0] * 26
            for ch in w:
                t[ord(ch) - ord("a")] += 1
            if all(t[i] >= c[i] for i in range(26)):
                a.append(w)
        return a


        