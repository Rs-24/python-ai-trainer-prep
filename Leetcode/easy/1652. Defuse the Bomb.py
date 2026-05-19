

class Solution:
    def decrypt(self, code: list, k: int) -> list:
        # Time: O(n * k), n = len(code)
        # Space: O(n)
        n = len(code)
        out = [0] * n
        if k == 0:
            return out
        for i in range(n):
            j = 1 if k > 0 else -1
            total = 0
            while abs(j) <= abs(k):
                total += code[(i + j) % n]
                j += 1 if k > 0 else -1
            out[i] = total
        return out


