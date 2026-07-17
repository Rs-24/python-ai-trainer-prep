

class Solution:
    def dailyTemperatures(self, temperatures: list) -> list:
        # Time: O(n)
        # Space: O(n)
        n = len(temperatures)
        o = [0] * n
        s = []
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                j = s.pop()
                o[j] = i - j
            s.append(i)
        return o


