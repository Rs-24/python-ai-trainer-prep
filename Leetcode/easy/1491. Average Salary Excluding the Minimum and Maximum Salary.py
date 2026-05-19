

class Solution:
    def average(self, salary: list) -> float:
        # Time: O(n), n = len(salary)
        # Space: O(1)
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)


