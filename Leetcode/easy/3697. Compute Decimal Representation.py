# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/compute-decimal-representation/description/

from typing import List

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        # Time: O(log n)
        # Space: O(log n)
        ans = []
        power = 0
        while n > 0:
            if n % 10 != 0:
                ans.append((n % 10) * (10 ** power))
            n //= 10
            power += 1
        return ans[::-1]


