

class Solution:
    def maximumPopulation(self, logs: list[list]) -> int:
        # Time: O(n), n = len(logs)
        # Space: O(1)
        y = [0] * 101
        for a, b in logs:
            for i in range(a, b):
                y[i - 1950] += 1
        best = max(y)
        for i, pop in enumerate(y):
            if pop == best:
                return i + 1950


