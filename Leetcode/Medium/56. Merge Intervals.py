

class Solution:
    def merge(self, intervals: list[list]) -> list[list]:
        # Time: O(n log n)
        # Space: O(n)
        intervals.sort(key=lambda x: x[0])
        out = []
        for a, b in intervals:
            if not out or a > out[-1][1]:
                out.append([a, b])
            else:
                out[-1][1] = max(out[-1][1], b)
        return out


