# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Time: O(n), n = len(operations)
        # Space: O(1)
        ans = 0
        for op in operations:
            ans += 1 if op[1] == "+" else -1
        return ans


