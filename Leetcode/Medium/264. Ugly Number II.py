

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        a = [1] * n
        i2 = i3 = i5 = 0
        for i in range(1, n):
            t2 = a[i2] * 2
            t3 = a[i3] * 3
            t5 = a[i5] * 5
            a[i] = min(t2, t3, t5)
            i2 += a[i] == t2
            i3 += a[i] == t3
            i5 += a[i] == t5
        return a[n - 1]


