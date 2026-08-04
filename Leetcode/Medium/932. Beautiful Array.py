

class Solution:
    def beautifulArray(self, n: int) -> list:
        # Time: O(n)
        # Space: O(n)
        if n == 1:
            return [1]
        o = self.beautifulArray((n + 1) // 2)
        e = self.beautifulArray(n // 2)
        return [2 * x - 1 for x in o] + [2 * x for x in e]


