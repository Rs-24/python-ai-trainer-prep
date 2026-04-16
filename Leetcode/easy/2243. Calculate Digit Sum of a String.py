# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Time: O(n * (m + log k)), n = number of rounds, m = len(s)
        # Aux space: O(m)
        def get_sum(x: int) -> int:
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total
        while len(s) > k:
            digits = []
            for i in range(0, len(s), k):
                digits.append(str(get_sum(int(s[i:i + k]))))
            s = "".join(digits)
        return s


