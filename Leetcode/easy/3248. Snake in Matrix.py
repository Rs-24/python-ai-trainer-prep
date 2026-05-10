# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/snake-in-matrix/description/

from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # Time: O(m), m = len(commands)
        # Space: O(1)
        pos = 0
        for c in commands:
            if c == "UP":
                pos -= n
            elif c == "RIGHT":
                pos += 1
            elif c == "DOWN":
                pos += n
            else:
                pos -= 1
        return pos


