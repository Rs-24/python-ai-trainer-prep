

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Time: O(n)
        # Space: O(1)
        num1 = num2 = 0
        for x in range(1, n + 1):
            if x % m == 0:
                num2 += x
            else:
                num1 += x
        return num1 - num2


