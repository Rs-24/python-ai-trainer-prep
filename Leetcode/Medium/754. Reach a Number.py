

class Solution:
    def reachNumber(self, target: int) -> int:
        # Time: O(n)
        # Space: O(1)
        i = t = 0
        while t < abs(target) or (t - target) % 2:
            i += 1
            t += i
        return i


