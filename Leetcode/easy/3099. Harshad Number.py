

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # Time: O(log x)#
        # Space: O(1)
        t = x
        s = 0
        while x > 0:
            s += x % 10
            x //= 10
        return s if t % s == 0 else -1


