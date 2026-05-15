

class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Time: O(log num)
        # Space: O(1)
        count = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1
        return count


