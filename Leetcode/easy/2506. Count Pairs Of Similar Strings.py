

class Solution:
    def similarPairs(self, words: list) -> int:
        # Time: O(n log n)
        # Space: O(n)
        d = {}
        ans = 0
        for w in words:
            s = "".join(sorted(set(w)))
            ans += d.get(s, 0)
            d[s] = d.get(s, 0) + 1
        return ans


