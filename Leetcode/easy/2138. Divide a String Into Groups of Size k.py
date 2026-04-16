# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # Time: O(n), n = len(s)
        # Aux space: O(k)
        out = []
        for i in range(0, len(s), k):
            temp = s[i:i + k]
            if len(temp) < k:
                temp += fill * (k - len(temp))
            out.append(temp)
        return out


