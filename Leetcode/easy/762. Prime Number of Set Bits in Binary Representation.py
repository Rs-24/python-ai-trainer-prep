# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Time: O((right - left + 1) * log right)
        # Space: O(1)
        def set_bits(x: int) -> int:
            total = 0
            while x > 0:
                x &= (x - 1)
                total += 1
            return total
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            i = 2
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 1
            return True
        count = 0
        for i in range(left, right + 1):
            count += 1 if is_prime(set_bits(i)) else 0
        return count


