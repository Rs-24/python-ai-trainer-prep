

class Solution:
    def sumOfEncryptedInt(self, nums: list) -> int:
        # Time: O(n log x)
        # Time: O(1)
        def encrypt(x: int) -> int:
            p = -1
            m = 0
            while x > 0:
                p += 1
                m = max(m, x % 10)
                x //= 10
            out = 0
            for i in range(p + 1):
                out += m * (10 ** i)
            return out
        return sum(encrypt(n) for n in nums)


