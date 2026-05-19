

class Solution:
    def maximumWealth(self, accounts: list[list]) -> int:
        # Time: O(m * n), m = len(accounts), n = len(accounts[0])
        # Space: O(1)
        return max(sum(row) for row in accounts)


