

class Solution:
    def twoCitySchedCost(self, costs: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        costs.sort(key=lambda x: x[1] - x[0])
        a = 0
        for i in range(len(costs) // 2):
            a += costs[i][1]
        for i in range(len(costs) // 2, len(costs)):
            a += costs[i][0]
        return a


