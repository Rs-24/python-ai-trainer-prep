# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/alternating-groups-i/description/

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        # Time: O(n), n = len(colors)
        # Space: O(1)
        n = len(colors)
        count = 0
        for i in range(n):
            if colors[i] != colors[(i - 1) % n] and colors[i] != colors[(i + 1) % n]:
                count += 1
        return count


