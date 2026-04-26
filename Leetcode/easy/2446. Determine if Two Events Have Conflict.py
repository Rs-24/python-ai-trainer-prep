# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/determine-if-two-events-have-conflict/description/

from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # Time: O(1)
        # Space: O(1)
        return not (event1[1] < event2[0] or event2[1] < event1[0])


