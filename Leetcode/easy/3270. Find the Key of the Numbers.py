

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # Time: O(1)
        # Space: O(1)
        a = "0" * (4 - len(str(num1))) + str(num1)
        b = "0" * (4 - len(str(num2))) + str(num2)
        c = "0" * (4 - len(str(num3))) + str(num3)
        return int("".join([min(a[i], b[i], c[i]) for i in range(4)]))


