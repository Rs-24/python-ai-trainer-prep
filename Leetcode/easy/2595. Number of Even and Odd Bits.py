# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/number-of-even-and-odd-bits/description/

from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        # Time: O(log n)
        # Space: O(1)
        even = 0
        odd = 0
        idx = 0
        while n > 0:
            if idx % 2 == 0:
                even += n & 1
            else:
                odd += n & 1
            idx += 1
            n >>= 1
        return [even, odd]


