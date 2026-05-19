

class Solution:
    def slowestKey(self, releaseTimes: list, keysPressed: str) -> str:
        # Time: O(n), n = len(releaseTimes) = len(keysPressed)
        # Space: O(1)
        best = 0
        letter = ""
        for i, k in enumerate(keysPressed):
            time = releaseTimes[i] if i == 0 else releaseTimes[i] - releaseTimes[i - 1]
            if time > best:
                best = time
                letter = k
            elif time == best:
                letter = max(letter, k)
        return letter


