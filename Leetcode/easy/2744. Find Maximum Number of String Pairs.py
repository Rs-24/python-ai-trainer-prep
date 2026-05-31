

class Solution:
    def maximumNumberOfStringPairs(self, words: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set()
        c = 0
        for w in words:
            if w[::-1] in s:
                c += 1
            else:
                s.add(w)
        return c


