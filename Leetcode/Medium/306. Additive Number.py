

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # Time: O(n^2)
        # Space: O(1)
        n = len(num)
        def v(a: int, b: int, i: int):
            while i < n:
                c = a + b
                if not num.startswith(str(c), i):
                    return False
                i += len(str(c))
                a, b = b, c
            return True
        for i in range(1, n):
            if num[0] == "0" and i > 1:
                break
            a = int(num[:i])
            for j in range(i + 1, n):
                if num[i] == "0" and j - i > 1:
                    break
                b = int(num[i:j])
                if v(a, b, j):
                    return True
        return False


