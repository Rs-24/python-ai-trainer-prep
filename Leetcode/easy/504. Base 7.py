

class Solution:
    def convertToBase7(self, num: int) -> str:
        # Time: O(log num)
        # Space: O(log num)
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        new = []
        while num > 0:
            new.append(str(num % 7))
            num //= 7
        new = "".join(reversed(new))
        return "-" + new if negative else new


