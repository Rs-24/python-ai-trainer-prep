

class Solution:
    def canMakePaliQueries(self, s: str, queries: list) -> list:
        # Time: O(n)
        # Space: O(n)
        prefix = [0] * (len(s) + 1)
        for i, ch in enumerate(s):
            prefix[i + 1] = prefix[i] ^ (1 << (ord(ch) - ord("a")))
        a = []
        for l, r, k in queries:
            a.append(((prefix[r + 1] ^ prefix[l]).bit_count()) // 2 <= k)


