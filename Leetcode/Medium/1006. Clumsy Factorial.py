

class Solution:
    def clumsy(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        s = [n]
        n -= 1
        t = 0
        while n > 0:
            if t == 0:
                s[-1] *= n
            elif t == 1:
                s[-1] = int(s[-1] / n)
            elif t == 2:
                s.append(n)
            else:
                s.append(-n)
            t = (t + 1) % 4
            n -= 1
        return sum(s)


