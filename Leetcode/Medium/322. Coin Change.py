# Time to write all of below including tests, explanation and time and aux
# and total space: 23 mins

# Problem: https://leetcode.com/problems/coin-change/description/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        out = dp[amount]
        return out if out != amount + 1 else -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange([1], 1) == 1
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([1], 5) == 5
    assert sol.coinChange([2], 1) == -1
    assert sol.coinChange([1, 2, 5], 13) == 4
    assert sol.coinChange([2, 5], 1) == -1
    assert sol.coinChange([5, 1, 2], 13) == 4
    assert sol.coinChange([5, 2], 1) == -1
    assert sol.coinChange([1, 3, 4], 6) == 2

# Explanation: the code stores dp, where each index stores the minimum number
# of coins to make up that amount. It then iterates across dp and calculates 
# the value for each index until it reaches amount
# Time: O(amount * n), n = len(coins)
# Aux space, excluding output and input: O(amount)
# Total space, including output, excluding input: O(amount)

# Breadth-first-search method:
from collections import deque
def coinChange(self, coins: List[int], amount: int) -> int:
    # Time: O(amount * n), n = len(coins)
    # Aux space, excluding output and input: O(amount)
    # Total space, including output, excluding input: O(amount)
    q = deque([(amount, 0)])
    visited = set()
    visited.add(amount)
    while q:
        remaining, num_steps = q.popleft()
        if remaining == 0:
            return num_steps
        for c in coins:
            nxt = remaining - c
            if nxt >= 0 and nxt not in visited:
                q.append((nxt, num_steps + 1))
                visited.add(nxt)
    return -1


