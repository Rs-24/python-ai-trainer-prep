

class Solution:
    def primePalindrome(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        if 8 <= n <= 11:
            return 11
        def p(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2
            return True
        t = 1
        while True:
            a, b = 10 ** (t - 1), 10 ** t
            for x in range(a, b):
                x = int(str(x) + str(x)[-2::-1])
                if x >= n and p(x):
                    return x
            t += 1


