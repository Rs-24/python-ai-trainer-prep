# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/

from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        # Time: O(m * n), m = ord(s[3]) + 1 - ord(s[0], n = int(s[4]) + 1 - int(s[1])
        # Aux space: O(1)
        out = []
        for i in range(ord(s[0]), ord(s[3]) + 1):
            for j in range(int(s[1]), int(s[4]) + 1):
                out.append(chr(i) + str(j))
        return out


