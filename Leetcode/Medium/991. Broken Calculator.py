

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        a = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            a += 1
        return a + (startValue - target)


