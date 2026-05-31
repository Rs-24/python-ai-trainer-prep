

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list, target: int) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(h >= target for h in hours)


