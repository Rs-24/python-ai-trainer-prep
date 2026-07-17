

class Solution:
    def magicalString(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        s = [1, 2, 2]
        i = 2
        x = a = 1
        while len(s) < n:
            for _ in range(s[i]):
                s.append(x)
                a += (len(s) <= n and x == 1)
            x = 3 - x
            i += 1
        return a


