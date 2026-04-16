# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Time: O(n + k log d), n = len(s), d = average number of digits
        # passed to sum_digits()
        # Aux space: O(n)
        def sum_digits(x: int) -> int:
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total
        total = []
        for ch in s:
            total.append(str(ord(ch) - ord("a") + 1))
        total = int("".join(total))
        for _ in range(k):
            total = sum_digits(total)
        return total


