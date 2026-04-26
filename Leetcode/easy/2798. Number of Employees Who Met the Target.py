# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/number-of-employees-who-met-the-target/description/

from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # Time: O(n), n = len(hours)
        # Space: O(1)
        return sum(h >= target for h in hours)


