

class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        # Time: O(n), n = len(timeSeries)
        # Space: O(1)
        total = 0
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]
            total += min(gap, duration)
        return total + duration


