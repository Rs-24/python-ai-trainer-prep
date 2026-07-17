

class Solution:
    def longestWord(self, words: list) -> str:
        # Time: O(n log n)
        # Space: O(n)
        words.sort()
        s = set()
        a = ""
        for w in words:
            if len(w) == 1 or w[:-1] in s:
                s.add(w)
                if len(w) > len(a):
                    a = w
        return a


