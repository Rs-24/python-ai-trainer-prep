# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/counting-bits/description/

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time: O(n log n)
        # Space, excluding output: O(1)
        def count(x: int) -> int:
            total = 0
            while x > 0:
                total += (x & 1)
                x >>= 1
            return total
        out = []
        for i in range(n + 1):
            out.append(count(i))
        return out

# Dynamic programming method: 
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time: O(n)
        # Space, excluding output: O(1)
        out = [0] * (n + 1)
        for i in range(1, n + 1):
            out[i] = out[i >> 1] + (i & 1)
        return out

