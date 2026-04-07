# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/slowest-key/description/

from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # Time: O(n), n = len(releaseTimes)
        # Space: O(1)
        best = 0
        letter = ""
        for i, t in enumerate(releaseTimes):
            time = t if i == 0 else t - releaseTimes[i - 1]
            if time > best:
                best = time
                letter = keysPressed[i]
            elif time == best:
                letter = max(letter, keysPressed[i])
        return letter


