

class Solution:
    def earliestFinishTime(self, landStartTime: list, landDuration: list, waterStartTime: list, waterDuration: list) -> int:
        # Time: O(n)
        # Space: O(1)
        def c(s1, d1, s2, d2) -> int:
            switch = min(s + d for s, d in zip(s1, d1))
            end = float("inf")
            for s, d in zip(s2, d2):
                end = min(end, max(switch, s) + d)
            return end
        return min(c(landStartTime, landDuration, waterStartTime, waterDuration), c(waterStartTime, waterDuration, landStartTime, landDuration))


