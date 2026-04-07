# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Time: O(n)
        # Space, excluding output: O(1)
        out = [0] * n
        i = 0
        while i < n // 2:
            out[i] = -(n // 2) + i
            i += 1
        i = n // 2 + 1
        while i < n:
            out[i] = i - n // 2
            i += 1
        if n % 2 == 0:
            out[n - 1] += (i - n // 2)
        return out

# Alternative version:
from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Time: O(n)
        # Space, excluding output: O(1)
        out = []
        for i in range(1, n // 2 + 1):
            out.append(i)
            out.append(-i)
        if n % 2 == 1:
            out.append(0)
        return out


