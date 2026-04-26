# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-losers-of-the-circular-game/description/

from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        # Time: O(n)
        # Aux space: O(n)
        visited = set()
        i = 0
        step = 1
        while i not in visited:
            visited.add(i)
            i = (i + step * k) % n
            step += 1
        return [i + 1 for i in range(n) if i not in visited]


