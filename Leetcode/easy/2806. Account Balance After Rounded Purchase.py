# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/account-balance-after-rounded-purchase/description/

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Time: O(1)
        # Space: O(1)
        digit = purchaseAmount % 10
        purchaseAmount //= 10
        if digit >= 5:
            purchaseAmount += 1
        purchaseAmount *= 10
        return 100 - purchaseAmount


