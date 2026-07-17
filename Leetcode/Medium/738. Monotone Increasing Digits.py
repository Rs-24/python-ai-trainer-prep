

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Time: O(d)
        # Space: O(d)
        a = list(str(n))
        t = len(a)
        for i in range(len(a) - 1, 0, -1):
            if a[i - 1] > a[i]:
                a[i - 1] = str(int(a[i - 1]) - 1)
                t = i
        for i in range(t, len(a)):
            a[i] = "9"
        return int("".join(a))


