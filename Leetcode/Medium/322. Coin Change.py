# Time to write all of below including tests, explanation and time and aux
# and total space: 23 mins

# Problem: https://leetcode.com/problems/coin-change/description/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        count = 0
        i = len(coins) - 1
        while amount >= 0 and i >= 0:           
            while amount >= 0:
                amount -= coins[i]
                count += 1
            amount += coins[i]
            count -= 1
            i -= 1
            if amount == 0:
                return count
        return -1

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

# Explanation: the code sorts coins and iterates through it from the end,
# while finding the max amount of each coin that can fit in amount
# Time: O(n log n + n * k), n = len(coins), k = average amount of each coin
# that can fit in variable 'amount'
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 23 mins):
#   - I now realise my solution is incorrect, my rewrite is below:
#
# def coinChange(self, coins: List[int], amount: int) -> int:
#     # Time: O(amount * n), n = len(coins)
#     # Aux space, excluding output and input: O(amount)
#     # Total space, including output, excluding input: O(amount)
#     dp = [amount + 1] * (amount + 1)
#     dp[0] = 0
#     for a in range(1, amount + 1):
#         for c in coins:
#             if a - c >= 0:
#                 dp[a] = min(dp[a], dp[a - c] + 1)
#     out = dp[amount]
#     return out if out != amount + 1 else -1
#
#   - Additionally, there is also a breadth-first-search version, my attempt
#     is below:
#
# from collections import deque
# def coinChange(self, coins: List[int], amount: int) -> int:
#     # Time: O(amount * n), n = len(coins)
#     # Aux space, excluding output and input: O(amount)
#     # Total space, including output, excluding input: O(amount)
#     q = deque([(amount, 0)])
#     visited = set()
#     visited.add(amount)
#     while q:
#         remaining, num_steps = q.popleft()
#         if remaining == 0:
#             return num_steps
#         for c in coins:
#             nxt = remaining - c
#             if nxt >= 0 and nxt not in visited:
#                 q.append((nxt, num_steps + 1))
#                 visited.add(nxt)
#     return -1
#
#   - Additionally, my tests could have been improved, my rewrite is below:
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.coinChange([1], 1) == 1
#     assert sol.coinChange([1], 0) == 0
#     assert sol.coinChange([1], 5) == 5
#     assert sol.coinChange([2], 1) == -1
#     assert sol.coinChange([1, 2, 5], 13) == 4
#     assert sol.coinChange([2, 5], 1) == -1
#     assert sol.coinChange([5, 1, 2], 13) == 4
#     assert sol.coinChange([5, 2], 1) == -1
#     assert sol.coinChange([1, 3, 4], 6) == 2












