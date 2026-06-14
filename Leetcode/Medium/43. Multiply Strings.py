

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Time: O(n^2)
        # Space: O(n)
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                x = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0")) + res[i + j + 1]
                res[i + j] += x // 10
                res[i + j + 1] = x % 10
        for i in range(len(res)):
            if res[i] != 0:
                return "".join(map(str, res[i:]))


