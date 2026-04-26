# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-symmetric-integers/description/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # Time: O(n), n = high - low
        # Space: O(1)
        def is_symmetric(x: int) -> bool:
            s = str(x)
            n = len(s)
            if n % 2 != 0:
                return False
            return sum(map(int, s[:n // 2])) == sum(map(int, s[n // 2:]))
        count = 0
        for x in range(low, high + 1):
            count += 1 if is_symmetric(x) else 0
        return count


