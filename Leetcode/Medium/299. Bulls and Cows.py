

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Time: O(1)
        # Space: O(1)
        b = 0
        s = [0] * 10
        g = [0] * 10
        for ch1, ch2 in zip(secret, guess):
            if ch1 == ch2:
                b += 1
            else:
                s[int(ch1)] += 1
                g[int(ch2)] += 1
        c = 0
        for x in range(10):
            c += min(s[x], g[x])
        return str(b) + "A" + str(c) + "B"


