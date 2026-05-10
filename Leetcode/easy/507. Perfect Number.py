

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Time: O(num ** 0.5)
        # Space: O(1)
        if num <= 1:
            return False
        total = 1
        for x in range(2, int(num ** 0.5) + 1):
            if num % x == 0:
                total += x
                if x != num // x:
                    total += num // x
        return total == num


