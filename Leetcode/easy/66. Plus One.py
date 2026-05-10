

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Time: O(n), n = len(digits)
        # Aux space: O(1)
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            d = digits[i] + carry
            digits[i] = d % 10
            carry = d // 10
        return [1] + digits if carry else digits


