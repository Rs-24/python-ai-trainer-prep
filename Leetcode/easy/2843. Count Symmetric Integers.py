

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # Time: O(n)
        # Space: O(1)
        def sym(x: int) -> bool:
            if len(str(x)) % 2 != 0:
                return False
            c = len(str(x)) // 2
            l, r = 0, 0
            while x > 0:
                if c > 0:
                    r += x % 10
                    c -= 1
                else:
                    l += x % 10
                x //= 10
            return l == r
        return sum(1 for x in range(low, high + 1) if sym(x))


