

class Solution:
    def superPow(self, a: int, b: list) -> int:
        # Time: O(n)
        # Space: O(1)
        t = 1
        a %= 1337
        for d in b:
            t = (pow(t, 10, 1337) * pow(a, d, 1337)) % 1337
        return t


