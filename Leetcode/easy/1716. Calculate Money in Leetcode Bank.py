# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/

class Solution:
    def totalMoney(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        total = 0
        day = 1
        week = 1
        while day <= n:
            total += ((day - 1) % 7 + week)
            day += 1
            week = (day - 1) // 7
        return total 


