

class Solution:
    def xorQueries(self, arr: list, queries: list) -> list:
        # Time: O(n)
        # Space: O(n)
        prefix = [0] * (len(arr) + 1)
        for i, num in enumerate(arr):
            prefix[i + 1] = prefix[i] ^ num
        return [prefix[r + 1] ^ prefix[l] for l, r in queries]


