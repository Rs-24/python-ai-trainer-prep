

class Solution:
    def lexicalOrder(self, n: int) -> list:
        # Time: O(n)
        # Space: O(n)
        a = []
        x = 1
        for _ in range(n):
            a.append(x)
            if x * 10 <= n:
                x *= 10
            else:
                while x % 10 == 9 or x + 1 > n:
                    x //= 10
                x += 1
        return a


