# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/toggle-light-bulbs/description/

from typing import List

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        # Time: O(n log n), n = len(bulbs)
        # Space: O(n)
        on = set()
        for b in bulbs:
            if b in on:
                on.remove(b)
            else:
                on.add(b)
        return sorted(on)


