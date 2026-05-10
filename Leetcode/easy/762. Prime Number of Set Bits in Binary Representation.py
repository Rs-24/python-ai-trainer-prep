

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Time: O(n * sqrt(log right)), n = right - left
        # Space: O(1)
        def set_bits(x: int):
            count = 0
            while x > 0:
                x &= (x - 1)
                count += 1
            return count
        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            d = 2
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 1
            return True
        return sum(is_prime(set_bits(x)) for x in range(left, right + 1))


