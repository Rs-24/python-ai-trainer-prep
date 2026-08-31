

from bisect import bisect_right

class Solution:
    def numSmallerByFrequency(self, queries: list, words: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        def f(s: str) -> int:
            return s.count(min(s))
        a, s = [], sorted(f(w) for w in words)
        for q in queries:
            a.append(len(s) - bisect_right(s, f(q)))
        return a


