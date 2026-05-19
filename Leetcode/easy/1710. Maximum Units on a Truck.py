

class Solution:
    def maximumUnits(self, boxTypes: list[list], truckSize: int) -> int:
        # Time: O(n log n), n = len(boxtypes)
        # Space: O(1)
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        count = 0
        for a, b in boxTypes:
            count += min(truckSize, a) * b
            truckSize -= min(truckSize, a)
        return count


