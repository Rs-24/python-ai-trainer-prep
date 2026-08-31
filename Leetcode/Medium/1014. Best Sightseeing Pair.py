

class Solution:
    def maxScoreSightseeingPair(self, values: list) -> int:
        # Time: O(n)
        # Space: O(1)
        t, a = values[0], float("-inf")
        for i in range(1, len(values)):
            a = max(a, t + values[i] - i)
            t = max(t, values[i] + i)
        return a


