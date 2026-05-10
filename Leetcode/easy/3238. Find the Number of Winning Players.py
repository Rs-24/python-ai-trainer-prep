# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-number-of-winning-players/description/

from typing import List

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # Time: O(n + m), m = len(pick)
        # Space: O(n)
        count = [[0] * 11 for _ in range(n)]
        ans = 0
        for x, y in pick:
            count[x][y] += 1
        return sum(max(count[i]) > i for i in range(n))


