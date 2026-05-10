# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/restore-finishing-order/description/

from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Time: O(m + n), m = len(order), n = len(friends)
        # Space: O(m + n)
        f = set(friends)
        return [x for x in order if x in f]


