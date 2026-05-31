

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        # Time: O(1)
        # Space: O(1)
        if purchaseAmount % 10 >= 5:
            purchaseAmount = purchaseAmount // 10 + 1
        else:
            purchaseAmount //= 10
        return 100 - 10 * purchaseAmount


