

class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        # Time: O(n)
        # Space: O(1)
        s = t = a = 0
        for i in range(len(gas)):
            d = gas[i] - cost[i]
            t += d
            s += d
            if t < 0:
                a = i + 1
                t = 0
        return a if s >= 0 else -1


