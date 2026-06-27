

from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        c = Counter(s)
        t = [0] * 10
        t[0] = c["z"]
        t[2] = c["w"]
        t[4] = c["u"]
        t[6] = c["x"]
        t[8] = c["g"]
        t[3] = c["h"] - t[8]
        t[5] = c["f"] - t[4]
        t[7] = c["s"] - t[6]
        t[1] = c["o"] - t[0] - t[2] - t[4]
        t[9] = c["i"] - t[5] - t[6] - t[8]
        return "".join(str(d) * t[d] for d in range(10))


