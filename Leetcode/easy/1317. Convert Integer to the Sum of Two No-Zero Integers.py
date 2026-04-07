# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/

from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Time: O(n log n)
        # Space: O(1)
        def no_zero(x: int) -> bool:
            while x > 0:
                if x % 10 == 0:
                    return False
                x //= 10
            return True
        for i in range(1, n // 2 + 1):
            if no_zero(i) and no_zero(n - i):
                return [i, n - i]


