# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/number-of-senior-citizens/description/

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # Time: O(n), n = len(details)
        # Space: O(1)
        return sum(int(d[11:13]) > 60 for d in details)


