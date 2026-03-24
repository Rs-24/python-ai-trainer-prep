# Time to write all of below including tests, explanation and time and aux
# and total space: 13 mins

# Problem: https://leetcode.com/problems/binary-watch/description/

from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Time: O(1)
        # Space, excluding output: O(1)
        out = []
        for h in range(12):
            for m in range(60):
                if (bin(h).count("1") + bin(m).count("1")) == turnedOn:
                    new_m = "0" + str(m) if m <= 9 else str(m)
                    out.append(str(h) + ":" + new_m)
        return out


