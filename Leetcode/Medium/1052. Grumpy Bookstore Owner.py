

class Solution:
    def maxSatisfied(self, customers: list, grumpy: list, minutes: int) -> int:
        # Time: O(n)
        # Space: O(1)
        s = sum(c * (1 - g) for c, g in zip(customers, grumpy))
        e = 0
        for i in range(minutes):
            e += customers[i] if grumpy[i] else 0
        m = e
        for i in range(minutes, len(customers)):
            e += customers[i] if grumpy[i] else 0
            e -= customers[i - minutes] if grumpy[i - minutes] else 0
            m = max(m, e)
        return s + m


