

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Time: O(n + k log n), n = len(s)
        # Space: O(n)
        def sum_digits(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        n = []
        for ch in s:
            n.append(str(ord(ch) - ord("a") + 1))
        n = int("".join(n))
        for _ in range(k):
            n = sum_digits(n)
        return n


